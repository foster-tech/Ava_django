 (function($) {
     $(document).ready(function() {
         function updateFabricaDropdown() {
             var fabricanteId = $('.fabricante-select').val();
             $('.fabrica-select option').hide();
             $('.fabrica-select option[data-fabricante-id="'+ fabricanteId +'"]').show();
         }

         $('.fabricante-select').change(updateFabricaDropdown);

         updateFabricaDropdown();
     });
 })(django.jQuery);