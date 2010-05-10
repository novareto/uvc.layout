$(document).ready(function() {

    jQuery.fn.inputChoice = function(params) {
        var options = {
            allowOwnInput: true,
            vocabularyName: null,
        }
        op = jQuery.extend(options, params);

        return this.each(function() {

            var self = jQuery(this);
            var name = self.attr('name');

            if (op.vocabularyName == null) {
              var targetURL = (self.closest('form').attr('action') + 
                           '/++optional-vocabulary++' + name);
            }
            else {
              var targetURL = op.vocabularyName;
            }

            // this is a test
            var vocabulary = {
                testvalue: "Test value",
                something: "Another value"
            }

            $.ajax({
                type: "GET",
                url: ,
                dataType: "json",
                async: false,
                success: function(data) {
                    if (data.success == true) {
                        success = true;
                        vocabulary = data.items;
                    } 
                }
            });

            var option = self.attr('id');
            var id = 'choice-' + option;
            var add = 'add-' + option;
            var form = 'form-' + option;

            var existing = self.val();
            if (existing && vocabulary[existing] == undefined) {
                vocabulary[existing] = existing;
            }

            var row = self.closest('div');
            row.append('<form id="' + form +'" class="popform">' +
                       '<input type="text" name="'+form+'" />' +
                       '<a class="submit">Add</a></form>' + 
                       '<div id="' + id + '"></div>');

            var wrapper = $("#" + id);
            var popform = $("#" + form).hide();

            self.remove();

            wrapper.append('<div class="spawned-options">' +
                           '<a href="#" id="'+add+'">Add an option</a>' +
                           '</div>');

            $.each(vocabulary, function(key, value) {
                wrapper.append(
                    ('<div class="spawned-options">' + 
                     '<input type="radio" value="'+key+
                     '" name="'+name+'" />' + value + '</div>'))
            });

            $('input[name='+name+']').filter(
                'input[value='+existing+']').attr('checked', true);

            $('#' + add).click(function(e){
                e.preventDefault();
                popform.fadeIn(500);
                popform.find("input").attr('value', '');
                popform.center();
                $(this).blur();
                popform.find("input").focus();
            });

            popform.find('a.submit').click(function(e) {
                value = popform.find('input[type=text]').val();
                wrapper.append(
                    ('<div class="spawned-options">' + 
                     '<input type="radio" value="'+value+
                     '" name="'+name+'" />' + value + '</div>'));
                popform.fadeOut(500);
                return false;
            });

        });

    }

    jQuery.fn.center = function(params) {
        var options = {
            vertical: true,
            horizontal: true
        }
        op = jQuery.extend(options, params);
        
        return this.each(function(){
            
        //initializing variables
            var $self = jQuery(this);
            //get the dimensions using dimensions plugin
            var width = $self.width();
            var height = $self.height();
            //get the paddings
            var paddingTop = parseInt($self.css("padding-top"));
            var paddingBottom = parseInt($self.css("padding-bottom"));
            //get the borders
            var borderTop = parseInt($self.css("border-top-width"));
            var borderBottom = parseInt($self.css("border-bottom-width"));
            //get the media of padding and borders
            var mediaBorder = (borderTop+borderBottom)/2;
            var mediaPadding = (paddingTop+paddingBottom)/2;
            //get the type of positioning
            var positionType = $self.parent().css("position");
            // get the half minus of width and height
            var halfWidth = (width/2)*(-1);
            var halfHeight = ((height/2)*(-1))-mediaPadding-mediaBorder;
            // initializing the css properties
            var cssProp = {
                position: 'absolute'
            };
            
            if(op.vertical) {
                cssProp.height = height;
                cssProp.top = '50%';
                cssProp.marginTop = halfHeight;
            }
            if(op.horizontal) {
                cssProp.width = width;
                cssProp.left = '50%';
                cssProp.marginLeft = halfWidth;
            }
            if(positionType == 'static') {
                $self.parent().css("position","relative");
            }
            $self.css(cssProp);
        });
    };

    $('body').append("<div id='loader'>&nbsp;</div>");
    
    $('body').ajaxStart(function() {
        loader = $("#loader");
        loader.addClass('loading');
        loader.center();
        loader.show();
    });

    $("#loader").ajaxStop(function() {
        $(this).removeClass('loading');
        $(this).hide();
    }); 


});
