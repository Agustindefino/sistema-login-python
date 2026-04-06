function startScanner(){

    navigator.mediaDevices.getUserMedia({ video: true })

    .then(stream => {

        const video = document.getElementById("video")

        video.srcObject = stream
        video.play()

    })
}

