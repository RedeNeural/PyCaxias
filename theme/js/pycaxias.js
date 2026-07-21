/* PyCaxias 2026 - comportamento da pagina
   Sem dependencias. Tudo degrada bem se o JS falhar. */

(function () {
  'use strict';

  var reduzirMovimento = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------------------------------------------------------------------
     Cabecalho fixo e barra de progresso
     --------------------------------------------------------------------- */
  var cabecalho = document.querySelector('.cabecalho');
  var progresso = document.querySelector('.progresso');

  function aoRolar() {
    var y = window.scrollY;

    if (cabecalho) {
      cabecalho.classList.toggle('esta-fixo', y > 40);
    }

    if (progresso) {
      var altura = document.documentElement.scrollHeight - window.innerHeight;
      var razao = altura > 0 ? Math.min(y / altura, 1) : 0;
      progresso.style.transform = 'scaleX(' + razao + ')';
    }
  }

  var aguardando = false;
  window.addEventListener('scroll', function () {
    if (aguardando) return;
    aguardando = true;
    window.requestAnimationFrame(function () {
      aoRolar();
      aguardando = false;
    });
  }, { passive: true });
  aoRolar();

  /* ---------------------------------------------------------------------
     Menu mobile
     --------------------------------------------------------------------- */
  var alternar = document.querySelector('.menu-alternar');
  var navegacao = document.querySelector('.navegacao');

  if (alternar && navegacao) {
    alternar.addEventListener('click', function () {
      var aberto = navegacao.classList.toggle('esta-aberta');
      alternar.setAttribute('aria-expanded', String(aberto));
      alternar.setAttribute('aria-label', aberto ? 'Fechar menu' : 'Abrir menu');
    });

    navegacao.addEventListener('click', function (evento) {
      if (evento.target.tagName === 'A') {
        navegacao.classList.remove('esta-aberta');
        alternar.setAttribute('aria-expanded', 'false');
      }
    });

    document.addEventListener('keydown', function (evento) {
      if (evento.key === 'Escape' && navegacao.classList.contains('esta-aberta')) {
        navegacao.classList.remove('esta-aberta');
        alternar.setAttribute('aria-expanded', 'false');
        alternar.focus();
      }
    });
  }

  /* ---------------------------------------------------------------------
     Trilho lateral: marca a secao em que a pessoa esta
     --------------------------------------------------------------------- */
  var paradas = Array.prototype.slice.call(document.querySelectorAll('.trilho__parada'));
  var secoes = paradas
    .map(function (parada) {
      var id = parada.getAttribute('href');
      return id ? document.querySelector(id) : null;
    })
    .filter(Boolean);

  if (secoes.length && 'IntersectionObserver' in window) {
    var observadorSecao = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (entrada) {
        if (!entrada.isIntersecting) return;
        paradas.forEach(function (parada) {
          parada.classList.toggle(
            'esta-ativa',
            parada.getAttribute('href') === '#' + entrada.target.id
          );
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });

    secoes.forEach(function (secao) { observadorSecao.observe(secao); });
  }

  /* ---------------------------------------------------------------------
     Revelar blocos ao entrar na tela
     --------------------------------------------------------------------- */
  var revelaveis = Array.prototype.slice.call(document.querySelectorAll('.revelar'));

  if (reduzirMovimento || !('IntersectionObserver' in window)) {
    revelaveis.forEach(function (elemento) { elemento.classList.add('esta-visivel'); });
  } else {
    var observadorRevelar = new IntersectionObserver(function (entradas, observador) {
      entradas.forEach(function (entrada) {
        if (!entrada.isIntersecting) return;
        entrada.target.classList.add('esta-visivel');
        observador.unobserve(entrada.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

    revelaveis.forEach(function (elemento) { observadorRevelar.observe(elemento); });
  }

  /* ---------------------------------------------------------------------
     Contagem regressiva
     --------------------------------------------------------------------- */
  var alvo = document.querySelector('[data-data-evento]');

  if (alvo) {
    var quando = new Date(alvo.getAttribute('data-data-evento')).getTime();

    var atualizar = function () {
      var restante = quando - Date.now();

      if (isNaN(quando)) {
        alvo.textContent = '';
        return;
      }
      if (restante <= 0) {
        alvo.textContent = 'e hoje';
        return;
      }

      var dias = Math.ceil(restante / 86400000);
      alvo.textContent = dias === 1 ? 'amanha' : 'faltam ' + dias + ' dias';
    };

    atualizar();
    setInterval(atualizar, 60000);
  }
})();
