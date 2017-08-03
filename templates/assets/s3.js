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

var params = 

var currentFiles = []  // All images currently in slideshow

function addImageToSlideShow(image_name) {

}

s3.listObjects(
  function(err, data) {
    if (err) console.log(err, err.stack); // an error occurred
    else {
      var availableFiles = data.Contents;  // successful response
      for (i=0; i<availableFiles.length; i++) {
        if (currentFiles.indexOf(availableFiles[i].Key) === -1) {
          currentFiles.push(availableFiles[i].Key);

        };
      };
    };
});

