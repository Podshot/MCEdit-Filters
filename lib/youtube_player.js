/**
 * @author Tomsik68
 */
function play(video){
	var videoLink = "http://www.youtube.com/embed/"+video;
	document.getElementById('youtube').src = videoLink;
	setTimeout('$("#videoplayer").show()',200);
}
