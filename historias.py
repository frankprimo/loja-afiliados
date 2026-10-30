
<!-- ===================================
     🌅 HISTÓRIA DO DIA
     =================================== -->

{% if historia_dia is defined %}

<section class="historia-dia">

    <span class="historia-etiqueta">
        ✨ MENSAGEM DO DIA
    </span>

    <h2>
        🌅 UM NOVO DIA, UMA NOVA HISTÓRIA
    </h2>

    <div class="historia-data">
        📅 {{ historia_dia.dia }},
        {{ historia_dia.data }}
    </div>

    <div class="historia-mensagem">
        {{ historia_dia.mensagem }}
    </div>

    <div class="historia-rodape">
        🌙 Amanhã: uma nova história te espera.
        <br>
        ✨ A mensagem de amanhã só será revelada quando o dia chegar.
    </div>

</section>

{% endif %}
