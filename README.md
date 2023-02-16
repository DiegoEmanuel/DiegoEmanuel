### Hi there 👋
✨ _special_ ✨ repository 
<img align="center" src="https://profile-counter.glitch.me/diegoemanuel/count.svg">
<div>
<a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/1680157/87443764-4af82c80-c5cc-11ea-82c2-c368ee12cf6d.png"><img alt="JavaScript" title="JavaScript" src="https://user-images.githubusercontent.com/1680157/87443764-4af82c80-c5cc-11ea-82c2-c368ee12cf6d.png" height="24" style="max-width: 100%;">  <a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/1680157/87443756-49c6ff80-c5cc-11ea-9052-ecd76bb5ce81.png"><img alt="Flutter" title="Flutter" src="https://user-images.githubusercontent.com/1680157/87443756-49c6ff80-c5cc-11ea-9052-ecd76bb5ce81.png" height="24" style="max-width: 100%;"> </a> </a> <a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/1680157/87443751-492e6900-c5cc-11ea-9854-f82d4d921133.png"><img alt="VS Code" title="VS Code" src="https://user-images.githubusercontent.com/1680157/87443751-492e6900-c5cc-11ea-9854-f82d4d921133.png" height="24" style="max-width: 100%;"></a> <a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/1680157/87443745-47fd3c00-c5cc-11ea-878f-44f34572775e.png"><img alt="Google Chrome" title="Google Chrome" src="https://user-images.githubusercontent.com/1680157/87443745-47fd3c00-c5cc-11ea-878f-44f34572775e.png" height="24" style="max-width: 100%;"></a> 

- 👯 I’m looking to collaborate on people who want to donate to find an easier association. ...
- 📫 How to reach me: 
  
  
  // music embed in top-left
// click beating heart to turn on lights
input#lighting(type="checkbox", name="lighting")
label(for="lighting")
.lighting-status
input#info(type="checkbox", name="info")
label(for="info")
.info-overlay
  h2 from the game
  a(href="http://store.steampowered.com/app/247080/", target="_blank")
    img(
      src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/168886/necrodancer-header.png"
    )
  h2 codepen by #[a(href="https://twitter.com/jhnsnc", target="_blank") Chris Johnson]
  p I'm just a fan of the game
  p I have no affiliation with the game or its creators
iframe.audio-embed(
  width=220,
  height=42,
  src="https://bandcamp.com/EmbeddedPlayer/album=441884888/size=small/bgcol=333333/linkcol=e99708/artwork=none/track=716340234/transparent=true/",
  seamless
)
  a(href="http://dbsoundworks.bandcamp.com/album/crypt-of-the-necrodancer-ost") Crypt of the Necrodancer OST by Danny Baranowsky
.container
  .floor
    - for (var r=2;r<13;r+=1)
      - for (var c=0;c<17;c+=1)
        div(class='floor-tile unlit ' + ((r + c) % 2 ? 'odd' : 'even') + ' pos-' + r + '-' + c)
        div(class='floor-tile lit ' + ((r + c) % 2 ? 'odd' : 'even') + ' pos-' + r + '-' + c)
  .walls
    - for (var r=0;r<13;r+=1)
      - for (var c=0;c<17;c+=1)
        if (r===0 && c>3 && c<13) || (r===1 && (c<5 || c>11)) || ((r>1 && r<12) && (c===0 || c===16)) || (r===9 && c===8) || (r===12)
          div(
            class='wall-tile type-' + Math.floor(1 + Math.random() * 5) + ' pos-' + r + '-' + c + (c === 2 || c === 10 || (r === 4 && c) || (r === 8 && !c) ? ' torch-left' : c === 6 || c === 14 || (r === 4 && !c) || (r === 8 && c) ? ' torch-right' : '')
          )
  .stage
    - for (var r=2;r<4;r+=1)
      - for (var c=5;c<12;c+=1)
        if (r===2) || (r===3 && (c<7 || c>9))
          div(class='stage-tile type-' + (r === 3 ? 3 : c === 5 || c === 11 ? 4 : 5 + (c % 2)) + ' pos-' + r + '-' + c)
  .characters
    .skeleton.pos-3-5
    .skeleton.pos-3-11
    .cadence.pos-7-6
    .dorian.mirrored.pos-8-10
    .golden-lute.pos-4-9
    .necrodancer.pos-5-6
