# Encoding = utf-8
import webbrowser
import os
import re

"""This python file contains methods used to generate a responsive html page. 
The web page abstracts a video library that enable users watch trailers of my 
favorite movies."""

__author__ = "Gustavo Nobrega"
__license__ = "GPL"
__version__ = "1.0"
__release__ = "1.0.1"
__maintainer__ = "Gustavo Nobrega"
__email__ = "gustavonobrega@gmail.com"
__status__ = "Production"


main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Home - Gustavo's Media Library Page!</title>

    <!-- CSS external youtube icon link -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    
    <!-- CSS Statements -->
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        
        body {
		padding: 60px 0px;
        }
        .navbar-collapse {
            position: relative;
            padding-top: 30px !important;
            max-height: 270px;
        }
        .navbar-collapse form[role="search"] {
            position: absolute;
            top: 0px;
            right: 0px;
            width: 100%;
            padding: 0px;
            margin: 0px;
            z-index: 0;
        }
        .navbar-collapse form[role="search"] button,
        .navbar-collapse form[role="search"] input {
            padding: 8px 12px;
            border-radius: 0px;
            border-width: 0px;
            color: rgb(119, 119, 119);
            background-color: rgb(248, 248, 248);
            border-color: rgb(231, 231, 231);
            box-shadow: none;
            outline: none;
        }
        .navbar-collapse form[role="search"] input {
            padding: 16px 12px;
            font-size: 14pt;
            font-style: italic;
            color: rgb(160, 160, 160);
            box-shadow: none;
        }
        .navbar-collapse form[role="search"] button[type="reset"] {
            display: none;
        }

        @media (min-width: 768px) {
            .navbar-collapse {
                padding-top: 0px !important;
                padding-right: 38px !important;
            }
            .navbar-collapse form[role="search"] {
                width: 38px;
            }
            .navbar-collapse form[role="search"] button,
            .navbar-collapse form[role="search"] input {
                padding: 15px 12px;
            }
            .navbar-collapse form[role="search"] input {
                font-size: 18pt;
                opacity: 0;
                display: none;            
                height: 50px;
            }
            .navbar-collapse form[role="search"].active {
                width: 100%;
            }
            .navbar-collapse form[role="search"].active button,
            .navbar-collapse form[role="search"].active input {
                display: table-cell;
                opacity: 1;
            }
            .navbar-collapse form[role="search"].active input {
                width: 100%;
            }
        }

        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }

        #myInput {
        background-image: url('/css/searchicon.png');
        background-position: 10px 12px;
        background-repeat: no-repeat;
        width: 100%;
        font-size: 16px;
        padding: 12px 20px 12px 40px;
        border: 1px solid #ddd;
        margin-bottom: 12px;
        }

        #myUL {
        list-style-type: none;
        padding: 0;
        margin: 0;
        }

        #myUL li a {
        border: 1px solid #ddd;
        margin-top: -1px; /* Prevent double borders */
        background-color: #f6f6f6;
        padding: 12px;
        text-decoration: none;
        font-size: 18px;
        color: black;
        display: block
        }

        #myUL li a:hover:not(.header) {
        background-color: #eee;
        }
  
    </style>
    
    <script type="text/javascript" charset="utf-8">

            //Alters visibility of element searched, case does not match the search  
            function myFunction(){
                var input, filter, ul, li, a, i;
                input = document.getElementById("myInput");
                filter = input.value.toUpperCase();
                ul = document.getElementById("myUL");
                li = ul.getElementsByTagName("li");         
                for (i = 0; i < li.length; i++) 
                {
                    a = li[i].getElementsByTagName("a")[0];
                    if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
                        li[i].style.display = "";
                    } else {
                        li[i].style.display = "none";
                    }
                }
            }
            
            //Set style visibility after scape from search field through exit button  
            function resetSearch(){ 
                var input, ul, li, i;
                input = document.getElementById("myInput");
                ul = document.getElementById("myUL");
                li = ul.getElementsByTagName("li");         
                for (i = 0; i < li.length; i++) 
                {
                    li[i].style.display = "";
                }
            }

            $(function () {
            // Remove Search if user Resets Form or hits Escape!
            $('body, .navbar-collapse form[role="search"] button[type="reset"]').on('click keyup', function(event) {
                console.log(event.currentTarget);
                if (event.which == 27 && $('.navbar-collapse form[role="search"]').hasClass('active') ||
                    $(event.currentTarget).attr('type') == 'reset') {
                    closeSearch();
                }
            });
            
            //Clears the search field when lefted
            function closeSearch() {
                var $form = $('.navbar-collapse form[role="search"].active')
                $form.find('input').val('');
                $form.removeClass('active');
            }

            // Show Search if form is not active // event.preventDefault() is important, this prevents the form from submitting
            $(document).on('click', '.navbar-collapse form[role="search"]:not(.active) button[type="submit"]', function(event) {
                event.preventDefault();
                var $form = $(this).closest('form'),
                    $input = $form.find('input');
                $form.addClass('active');
                $input.focus();

            });
            // ONLY FOR DEMO // Please use $('form').submit(function(event)) to track from submission
            // if your form is ajax remember to call `closeSearch()` to close the search container
            $(document).on('click', '.navbar-collapse form[role="search"].active button[type="submit"]', function(event) {
                event.preventDefault();
                var $form = $(this).closest('form'),
                    $input = $form.find('input');
                $('#showSearchTerm').text($input.val());
                closeSearch()
            });
        });
        
        
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        
        
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' +
                            trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
  <body>
        <!-- Trailer Video Modal -->
        <div class="modal" id="trailer">
        <div class="modal-dialog">
            <div class="modal-content">
            <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_
                        MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
            </a>
            <div class="scale-media" id="trailer-video-container">
            </div>
            </div>
        </div>
        </div>

        <!-- Main Page Content -->
        <nav class="navbar navbar-default navbar-fixed-top" role="navigation">
            <div class="container">
                <!-- Brand and toggle get grouped for better mobile display -->
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" 
                    data-target="#bs-example-navbar-collapse-1">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="#">Gustavo's Media Library Page</a>
                </div>

                <!-- Collect the nav links, forms, and other content for toggling -->
                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">				
                    <ul class="nav navbar-nav navbar-right">
                        <li><a href="https://youtube.com/"><i class="fa fa-youtube-play" 
                            style="font-size:24px;color:red;padding-right:5px;"></i>Youtube</a></li>
                    </ul>

                    <form class="navbar-form" role="search">
                        <div class="input-group">
                            <input id="myInput" type="text" onkeyup="myFunction()" 
                            class="form-control" placeholder="Search">
                            <span class="input-group-btn">
                                <button type="reset" class="btn btn-default" onclick="resetSearch()">
                                    <span class="glyphicon glyphicon-remove">
                                        <span class="sr-only">Close</span>
                                    </span>
                                </button>
                                <button type="submit" class="btn btn-default" onclick="resetSearch()">
                                    <span class="glyphicon glyphicon-search">
                                        <span class="sr-only">Search</span>
                                    </span>
                                </button>
                            </span>
                        </div>
                    </form>
                </div><!-- /.navbar-collapse -->
            </div><!-- /.container-fluid -->
        </nav>
        <div class="container">
        <ul id="myUL">
        {movie_tiles}
        </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
    <li class="movie-tile2">
        <div class="col-md-6 col-lg-4 movie-tile text-center" style="display: block;" 
        data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
            <img src="{poster_image_url}" width="220" height="342">
            <a href="#"><h4>{movie_title}</h4></a>
            <h4>Duration: {movie_duration}</h4>
        </div>
    </li>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_duration=movie.duration,
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content + "</ul>")
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)


def open_movies_page_tv_station(tv_station):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(tv_station))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
