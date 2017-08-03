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

var params = {
  Bucket: 'groove-booth', /* required */
};

var currentFiles = []

function encode(data)
{
    var str = data.reduce(function(a,b){ return a+String.fromCharCode(b) },'');
    return btoa(str).replace(/.{76}(?=.)/g,'$&\n');
}

s3.listObjects(params, function(err, data) {
  if (err) console.log(err, err.stack); // an error occurred
  else {
    var availableFiles = data.Contents;  // successful response
    for (i=0; i<availableFiles.length; i++) {
      if (currentFiles.indexOf(availableFiles[i].Key) === -1) {
        currentFiles.push(availableFiles[i].Key);
        console.log(currentFiles)
        s3.getObject({Key: availableFiles[i].Key},function(err,file){
          $timeout(
            function(){
              $scope.s3url = "data:image/jpeg;base64," + encode(file.Body);
            },
            1
          )
        });
      };
    };
  };
};