$(document).ready(function() {
   /*
   $(document).on('click', '.glyphicon', function() {
      var key = $(this).attr('key');
      $.get('/testbrowser/testreport/', {'key': key}, function(data) {
         //alert(data.key);
         //alert(JSON.stringify(data.testresults));

         $("#dialog_report_modal").find(".modal-title").html(data.key + " Test Report");
         
         var barHeight = 10;
         var svg = d3.select("svg")
                     .attr("height", barHeight * data.testresults.length);
                     
         max = d3.max(data.testresults, function(d) {
            return d.dcount;
         });
                     
         var scale = d3.scale.linear()
                             .domain([0, max]).range([0, 800]);
                             
         var barGroup = svg.append("g");
         
         barGroup.selectAll("rect")
            .data(data.testresults)
            .enter()
            .append("rect")
            .attr("x", 0)
            .attr("y", function(d, i) { return barHeight * i; })
            .attr("width", function(d) { return scale(d.dcount); })
            .attr("height", 9)
            .style("fill", "steelblue");
      });
   });
   */
   
   $(document).on('click', '.progress', function() {
      /*
      var cell = $(this).parent().parent();

      if (cell.attr('width') == '70%') {
         cell.attr('width', '0');
      } else {
         cell.attr('width', '70%');
      }
      
      $(this).children().find("span").toggleClass("sr-only");
      $('html,body').animate({scrollTop: $(this).offset().top - 200},'slow');
      */
      
      var id = $(this).parent().attr('href');
      var table_content = $(id + ".collapse").html();
      $(this).children().find("span").toggleClass("sr-only");
      var progressbar = $(this).parent().html();
      $("#dialog_lg_modal").find(".modal-title").html("Test Case " + id.replace('#', '') + " Execution History");
      $("#dialog_lg_modal").find(".modal-body").html(progressbar + table_content);
      $(this).children().find("span").toggleClass("sr-only");
   });
   
   /*
   $(document).on('click', '.glyphicon-file', function() {
      var key = $(this).parent().attr('href').replace('#', '');
      $("#dialog_report_modal").find(".modal-title").html(key + " Test Report");
   });
   */
   
   $(document).on('click', 'a.btn', function(){
      
      var filters = [];
      var clicked_text = $(this).text();
      var elements = '';
      
      // remove active except clicked one
      $.each($(this).parent().find('a.btn'), function() {
         if ($(this).text() != clicked_text) {
            $(this).removeClass('active'); 
         }
      });
      
      $(this).toggleClass('active');
      
      $.each($("a.btn.active"), function() {
         switch ($(this).parent().attr('id')) {
            case 'reglevel':
               filters.push("[reglevel*='" + $(this).text() + "']");
               break;
            case 'priority':
               filters.push("[priority*='" + $(this).text() + "']");
               break;
            case 'requirement':
               filters.push("[requirement*='" + $(this).text() + "']");
               break;
            case 'secondary_domain':
               filters.push("[secondary_domain*='" + $(this).text() + "']");
               break;
            case 'component':
               filters.push("[component*='" + $(this).text() + "']");
               break;
            case 'secondary':
               filters.push("[secondary*='" + $(this).text() + "']");
               break;
            case 'status':
               filters.push("[status*='" + $(this).text() + "']");
               break;
            case 'labels':
               filters.push("[labels*='" + $(this).text() + "']");
               break;
            case 'test_type':
               filters.push("[labels*='" + 'TYPE-' + $(this).text() + "']");
               break;
            case 'feature':
               filters.push("[labels*='" + 'FTR-' + $(this).text() + "']");
               break;
         }
      });
      
      switch ($('#issuetype').find('.dropdown-toggle').text().trim()) {
         case 'Test Case':
            $(".row_data").hide();
            elements = ".row_data" + filters.join('');
            $('#total_selected').html($(elements).length + ' testcases are selected.');
            break;
         case 'Test Plan':
            $("#accordion").children().hide();
            elements = ".panel" + filters.join('');
            $('#total_selected').html($(elements).length + ' testplans are selected.');
            break;
      }
   
      $(elements).show();
   });
   
   /*
   $(".btn-group-vertical").click(function() {
      var secondaries = [];
      var status = [];
      
      // add all the active or selected domains
      $(this).find(".btn-info.active").each(function() {
         secondaries.push($(this).text());
      });
      
      // add all active status
      $(this).find(".btn-success.active").each(function() {
         status.push($(this).text());
      })
      
      $(this).find(".btn-warning.active").each(function() {
         status.push($(this).text());
      });
      
      $(this).find(".btn-primary.active").each(function() {
         status.push($(this).text());
      })
      
      $(this).find(".btn-info:focus").each(function() {
         // if the current state is active, it means the selection will be toogled out, so
         // remove from the list
         //alert($(this).text() + ', ' + $(this).hasClass("active"));
         
         if ($(this).hasClass("active")) {
            var index = secondaries.indexOf($(this).text());
            //alert(index + '\n' + secondaries + '\n' + secondaries.length) ;
            if (index > -1) {
               secondaries.splice(index, 1);
            }
         } else {
            secondaries.push($(this).text());
         }
         
         // unfocus the element
         $(this).blur();
      });
      
      $(this).find(".btn-success:focus").each(function() {
         if ($(this).hasClass("active")) {
            var index = status.indexOf($(this).text());
          
            if (index > -1) {
               status.splice(index, 1);
            }
         } else {
            status.push($(this).text());
         }
         
         // unfocus the element
         $(this).blur();
      });
      
      $(this).find(".btn-warning:focus").each(function() {
         if ($(this).hasClass("active")) {
            var index = status.indexOf($(this).text());
          
            if (index > -1) {
               status.splice(index, 1);
            }
         } else {
            status.push($(this).text());
         }
         
         // unfocus the element
         $(this).blur();
      });
      
      $(this).find(".btn-primary:focus").each(function() {
         if ($(this).hasClass("active")) {
            var index = status.indexOf($(this).text());
          
            if (index > -1) {
               status.splice(index, 1);
            }
         } else {
            status.push($(this).text());
         }
         
         // unfocus the element
         $(this).blur();
      });
      
      // hide all - initialization
      $("div[secondary]").hide();
      $("div[status]").hide();

      if (secondaries.length == 0 && status.length > 0) {  
         $.each(status, function(index, status) {
            $("div[status*='" + status + "']").show();
         });
      } else if (status.length == 0 && secondaries.length > 0) {
         $.each(secondaries, function(index, secondary) {
            $("div[secondary*='" + secondary + "']").show();
         });
      } else if (secondaries.length == 0 && status.length == 0) {
         $("div[secondary]").show();
      } else if (secondaries.length > 0 && status.length > 0) {
         $.each(secondaries, function(index, secondary) {
            $.each(status, function(index, status) {
               $("div[secondary*='" + secondary + "'][status*='" + status + "']").show();
            });
         })
      }
      
      // set primary name
      $('#primary').html($('#primary_btn').text());
      
      // sort the secondaries
      secondaries.sort();
      $('#secondary').html(secondaries.join(", "));
      
      /*
      // process retrieve test plans for the selected domain
      $.get('/testbrowser/list_testplans/', {'primary': primary, 'secondary': secondaries.join(", ")}, function(data) {
         $('#testplans').html(data);
         $('.collapse').collapse(); // collapse all views
         
         // hide all SUP Portal
         $.each(secondaries, function( index, value) {
            alert(value);
            $("div[secondary*='" + value + "']").hide();
         });
      });
   });
   */
   
   /*
   $("#btn_testplan_load").click(function() {
      var secondaries = [];
      
      $("#secondaries").find(".btn.btn-primary.active").each(function() {
         secondaries.push($(this).text());
      });
      
      alert(secondaries);
   });
   */
   
   //dropdown-menu item selection handler
   $(".dropdown-menu li a").click(function() {
      
      var seltext = $(this).text();
      
      // update selected item's text
      $(this).parents(".dropdown").find('.dropdown-toggle').html(seltext + ' <span class="caret"></span>');
      
      var issuetype = $('#issuetype').find('.dropdown-toggle').text().trim();
      var primary = $('#primary_domain').find('.dropdown-toggle').text().trim();
      
      if (primary != 'Primary Domain') {
         $('#dialog_modal').find('.modal-body').text('Loading ' + primary + ' ' + issuetype + '...');
         $('#dialog_modal').modal('show');
         
         if (issuetype == 'Test Plan' && primary != 'Primary Domain') {
            // process retrieve test plans for the selected domain
            $.get('/testbrowser/list_testplans/', {'primary': primary}, function(data) {
               $('#list_data').html(data);
               $('.collapse').collapse(); // collapse all views
               $('#dialog_modal').modal('hide');
            });
         } else if (issuetype == 'Test Case' && primary != 'Primary Domain') {
            // process retrieve test cases for the selected domain
            $.get('/testbrowser/list_testcases/', {'primary': primary}, function(data) {
               $('#list_data').html(data);
               $('#dialog_modal').modal('hide');
            });
         }
      } else {
         $(".jumbotron").find('h1').text(seltext);
         $(".jumbotron").find('p').text('Please select primary domain to load ' + seltext + '.');
      }
      
      /*
      if ($(this).parents(".btn-group").attr('id') == 'primary_domain_dropdown') {
         var selText = $(this).text();
         
         // update selected item's text
         $(this).parents(".btn-group").find('.dropdown-toggle').html(selText + ' <span class="caret"></span>');
         
         // get the issue type
         var issuetype = $('#issuetype').find('label.active').text().trim();
         
         $('#dialog_modal').find('.modal-body').text('Loading ' + issuetype + '...');
         $('#dialog_modal').modal('show');
         
         if (issuetype == 'Test Plan') {
            /*
            // update with secondary domains for the selected primary domain
            $.get('/testbrowser/list_secondary/', {'sel_domain': selText}, function(data) {
               $('#filter').html(data);
               
               // process retrieve test plans for the selected domain
               $.get('/testbrowser/list_testplans/', {'primary': selText}, function(data) {
                  $('#list_data').html(data);
                  $('.collapse').collapse(); // collapse all views
                  //$("div[secondary]").hide();
                  $('#dialog_modal').modal('hide');
               });
            });
            
            // process retrieve test plans for the selected domain
            $.get('/testbrowser/list_testplans/', {'primary': selText}, function(data) {
               $('#list_data').html(data);
               $('.collapse').collapse(); // collapse all views
               $('#dialog_modal').modal('hide');
            });
         } else if (issuetype == 'Test Case') {
            // process retrieve test cases for the selected domain
            $.get('/testbrowser/list_testcases/', {'primary': selText}, function(data) {
               $('#list_data').html(data);
               $('#dialog_modal').modal('hide');
            });
         }
      }*/
   });
   
   // issue type selection button click event handler - Test Plan / Test Case
   $('.btn-default').click(function() {
      if ($(this).parents().attr('id') == 'issuetype') {
         $('#list_data').find('h1').html($(this).text().trim());
      }
   });   

   // when select secondaries links handler
   /*
   $('#secondaries').bind('click', function(event) {
      var secondary = event.target.text;
      var primary = $('#primary_btn').text();
      
      // process retrieve test plans for the selected domain
      $.get('/testbrowser/list_testplans/', {'primary': primary, 'secondary': secondary}, function(data) {
         $('#domain').html(data);
      });
   });
   */
});