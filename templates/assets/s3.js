var albumBucketName = 'groove-booth';
var bucketRegion = 'us-west-2';
var IdentityPoolId = 'us-west-2:868748e9-d131-43bf-ba84-aa645960611c';

AWS.config.update({
  region: bucketRegion,
  credentials: new AWS.CognitoIdentityCredentials({
    IdentityPoolId: IdentityPoolId
  })
});

var s3 = new AWS.S3({
  apiVersion: '2006-03-01',
  params: {Bucket: albumBucketName}
});

var MAX_N_FILES = 6
var currentFiles = []  // All images currently in slideshow
var timeoutHasBeenSet = false

function getNewImages() {
  s3.listObjects(
    {Bucket: albumBucketName}, 
    function(err, data) {
      if (err) console.log(err, err.stack); // an error occurred
      else {

        console.log("Searching for new images");

        var availableFiles = data.Contents;  // successful response

        for (i=0; i<availableFiles.length; i++) {

          if (currentFiles.indexOf(availableFiles[i].Key) === -1) {
            currentFiles.push(availableFiles[i].Key);

            var img_div = jQuery(
              "<div></div>", 
              {
                class: "mySlides fade"
              }
            );

            var img_link = jQuery(
              "<img></img>", 
              {
                src: "http://s3-us-west-2.amazonaws.com/groove-booth/" + availableFiles[i].Key,
                style: "width:100%"
              }
            );

            img_link.appendTo(img_div)
            img_div.appendTo($(".slideshow-container"))
          };
        };
        
        if ($(".slideshow-container").children().length > MAX_N_FILES) {
          $(".mySlides").first().remove();
        }

        if (!timeoutHasBeenSet) {
          setInterval(getNewImages, 60000);  // search for new images every minute
          timeoutHasBeenSet = true;
        };
        
      };
  });
};

getNewImages();

