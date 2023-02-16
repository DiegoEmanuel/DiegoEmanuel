### Hi there 👋
✨ _special_ ✨ repository 
<img align="center" src="https://profile-counter.glitch.me/diegoemanuel/count.svg">
<div>
<a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/1680157/87443764-4af82c80-c5cc-11ea-82c2-c368ee12cf6d.png"><img alt="JavaScript" title="JavaScript" src="https://user-images.githubusercontent.com/1680157/87443764-4af82c80-c5cc-11ea-82c2-c368ee12cf6d.png" height="24" style="max-width: 100%;">  <a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/1680157/87443756-49c6ff80-c5cc-11ea-9052-ecd76bb5ce81.png"><img alt="Flutter" title="Flutter" src="https://user-images.githubusercontent.com/1680157/87443756-49c6ff80-c5cc-11ea-9052-ecd76bb5ce81.png" height="24" style="max-width: 100%;"> </a> </a> <a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/1680157/87443751-492e6900-c5cc-11ea-9854-f82d4d921133.png"><img alt="VS Code" title="VS Code" src="https://user-images.githubusercontent.com/1680157/87443751-492e6900-c5cc-11ea-9854-f82d4d921133.png" height="24" style="max-width: 100%;"></a> <a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/1680157/87443745-47fd3c00-c5cc-11ea-878f-44f34572775e.png"><img alt="Google Chrome" title="Google Chrome" src="https://user-images.githubusercontent.com/1680157/87443745-47fd3c00-c5cc-11ea-878f-44f34572775e.png" height="24" style="max-width: 100%;"></a> 

- 👯 I’m looking to collaborate on people who want to donate to find an easier association. ...
- 📫 How to reach me: 
  
  @import "compass";

/**
 * VARIABLES
 */
$imgHost: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/168886/';
$bgCharacters: url($imgHost+'necrodancer-characters.png');
$bgRoom: url($imgHost+'necrodancer-room.png');

$beatTime: 60000ms / 160; // at 160bpm
$beatSwingStrength: 0.8;
/**
 * FUNCTIONS
 */
@function pi() {
  @return 3.14159265359;
}
@function factorial($x) {
  $value: 1;
  @if $x > 0 {
    @for $i from 1 through $x {
      $value: $value * $i;
    }
  }
  @return $value;
}
// Taylor series approximation. Increase iterations for higher accuracy
@function sin($theta, $iterations: 10) {
  $sin: 0;
  @for $i from 0 through $iterations {
    $sin: $sin + pow(-1, $i) * pow($theta, (2 * $i + 1)) / factorial(2 * $i + 1);
  }
  @return $sin;
}
// Taylor series approximation. Increase iterations for higher accuracy
@function cos($theta, $iterations: 10) {
  $cos: 0;
  @for $i from 0 through $iterations {
    $cos: $cos + pow(-1, $i) * pow($theta, 2 * $i) / factorial(2 * $i);
  }
  @return $cos;
}
@function beat-swing($x){
  @return pow( -1 * cos($x * pi() / 2) + 1, $beatSwingStrength); //in
  // @return pow( sin($x * pi() / 2), $beatSwingStrength); //out
}
@mixin sharp-pixels {
  -ms-interpolation-mode: nearest-neighbor; // IE 7+ (non-standard property)
  image-rendering: -webkit-optimize-contrast; // Safari 6, UC Browser 9.9
  image-rendering: -webkit-crisp-edges; // Safari 7+
  image-rendering: -moz-crisp-edges; // Firefox 3.6+
  image-rendering: -o-crisp-edges; // Opera 12
  image-rendering: pixelated; // Chrome 41+ and Opera 26+
}
/**
 * GENERAL
 */
html, body {
  width: 100%;
  height: 100%;
}
body {
  background: #060709;
}
.container {
  @include sharp-pixels;
  position: absolute;
  left: 50%;
  top: 50%;
  width: 17*24px;
  height: 14*24px;
  transform: translate(-50%, -50%) scale(2);
}
//positioning
@for $r from 0 through 13 {
  @for $c from 0 through 17 {
    .pos-#{$r}-#{$c} {
      position: absolute;
      left: $c * 24px;
      top: $r * 24px;
    }
  }
}
/**
 * CONTROLS
 */
input#lighting {
  display: none;
  + label {
    @include sharp-pixels;
    cursor: pointer;
    z-index: 20;
    position: absolute;
    left: 40%;
    bottom: 50px;
    display: block;
    width: 41px;
    height: 52px - 1;
    transform: scale(2) translate(-100%, 0%);
    transform-origin: 100% 50%;
    background: $bgRoom no-repeat;
    background-position: 0 -135px;
    animation: $beatTime step-end infinite heartbeat-pulse;
  }
  ~ .lighting-status {
    @include sharp-pixels;
    z-index: 20;
    position: absolute;
    left: 40%;
    bottom: 50px;
    display: block;
    width: 144px;
    height: 12px - 1;
    transform: scale(2) translate(0, -50%);
    transform-origin: 0 50%;
    background: $bgRoom no-repeat;
    background-position: 0 -199px;
  }
  &:checked {
    + label {
      filter: drop-shadow(0 0 3px rgba(#6cdaff, 0.8));
    }
    ~ .lighting-status {
      background-position: 0 -187px;
    }
  }
}
@keyframes heartbeat-pulse {
  0% { background-position: -41px -135px; }
  #{beat-swing(0.4) * 100}% { background-position: 0 -135px; }
}
.info-overlay {
  @include sharp-pixels;
  z-index: 10;
  position: absolute;
  left: 0;
  top: 0;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  padding: 3rem;
  text-align: center;
  background: rgba(#060709, 0.8);
  opacity: 0;
  transition: opacity 600ms;
  h2 {
    padding: 3rem 0 1.5rem;
    margin: 0;
    color: #ffffff;
    font-family: Helvetica, sans-serif;
    font-size: 36px;
  }
  p {
    color: #ffffff;
    font-family: Helvetica, sans-serif;
    font-size: 24px;
  }
  a {
    color: #6cdaff;
    text-decoration: none;
    &:hover, &:focus {
      color: #6cdaff;
      text-decoration: none;
      border-bottom: 2px solid #6cdaff;
    }
  }
}
input#info {
  display: none;
  + label {
    @include sharp-pixels;
    cursor: pointer;
    z-index: 30;
    position: absolute;
    right: 10px;
    top: 10px;
    display: block;
    width: 62px;
    height: 22px;
    background: $bgRoom no-repeat;
    background-position: -82px -135px;
    transform: scale(2);
    transform-origin: right top;
  }
  &:checked {
    ~ .info-overlay {
      opacity: 1.0;
    }
  }
}
.audio-embed {
  z-index: 30;
  position: relative;
  width: 220px;
  height: 42px;
  border: 0;
}
/**
 * FLOOR
 */
.floor-tile {
  width: 24px;
  height: 24px;
  background: $bgRoom no-repeat;
  &.odd {
    background-position: -1px -110px;
    &.unlit { animation: $beatTime*2 step-end infinite floor-pulse-unlit-odd; }
    &.lit { animation: $beatTime*2 step-end infinite floor-pulse-lit-odd; }
  }
  &.even {
    background-position: -27px -110px;
    &.unlit { animation: $beatTime*2 step-end infinite floor-pulse-unlit-even; }
    &.lit { animation: $beatTime*2 step-end infinite floor-pulse-lit-even; }
  }
  &.unlit { opacity: 1.0; }
  &.lit { opacity: 0.0; }
}
input#lighting:checked ~ .container .floor-tile {
  &.unlit { opacity: 0.0; }
  &.lit { opacity: 1.0; }
}
@keyframes floor-pulse-lit-odd {
  0% { background-position: -1px -110px; }
  50% { background-position: -53px -110px; }
}
@keyframes floor-pulse-lit-even {
  0% { background-position: -79px -110px; }
  50% { background-position: -27px -110px; }
}
@keyframes floor-pulse-unlit-odd {
  0% { background-position: -1px -110px; }
  50% { background-position: -27px -110px; }
}
@keyframes floor-pulse-unlit-even {
  0% { background-position: -27px -110px; }
  50% { background-position: -1px -110px; }
}
/**
 * WALLS
 */
%torch {
  display: block;
  width: 12px;
  height: 26px;
  background: $bgRoom no-repeat;
  background-position: -120px -61px;
  animation: $beatTime step-end infinite torch-flicker;
}
@keyframes torch-flicker {
  0% { background-position: -120px -61px; }
  #{beat-swing(0.25) * 100}% { background-position: -132px -61px; }
  #{beat-swing(0.50) * 100}% { background-position: -120px -87px; }
  #{beat-swing(0.75) * 100}% { background-position: -132px -87px; }
}
.wall-tile {
  width: 24px;
  height: 48px;
  background: $bgRoom no-repeat;
  transform: translateY(8px);
  @for $i from 1 through 5 {
    &.type-#{$i} {
      background-position: (($i - 1) * -24px) -61px;
    }
  }
  &.torch-left {
    &:after {
      content: ' ';
      @extend %torch;
      transform: translate(6px, -9px);
    }
  }
  &.torch-right {
    &:after {
      content: ' ';
      @extend %torch;
      transform: translate(6px, -9px) scaleX(-1);
    }
  }
}
/**
 * STAGE
 */
.stage-tile {
  width: 24px;
  height: 61px;
  background: $bgRoom no-repeat;
  transform: translateY(-35px);
  @for $i from 1 through 6 {
    &.type-#{$i} {
      background-position: (($i - 1) * -24px) 0px;
    }
  }
}
/**
 * SKELETONS
 */
.skeleton {
  width: 24px;
  height: 25px;
  background: $bgCharacters no-repeat;
  background-position: 0 -183px;
  animation: $beatTime*2 step-end infinite skeleton-dance;
  transform: translateY(-16px);
}
@keyframes skeleton-dance {
  @for $i from 0 through 7 {
    #{beat-swing(($i % 4) / 4) * 50 + if($i >= 4, 50, 0)}% { background-position: ($i * -24px) -183px; }
  }
}
/**
 * CADENCE
 */
.cadence {
  width: 24px;
  height: 24px;
  background: $bgCharacters no-repeat;
  background-position: 0 -159px;
  animation: $beatTime step-end infinite cadence-dance;
  transform: translate(0, -9px);
}
@keyframes cadence-dance {
  @for $i from 0 through 4 {
    #{beat-swing($i / 4) * 100}% { background-position: ($i * -24px) -159px; }
  }
}
/**
 * DORIAN
 */
.dorian {
  width: 33px;
  height: 32px;
  background: $bgCharacters no-repeat;
  background-position: 0 -94px;
  animation: $beatTime step-end infinite dorian-dance;
  transform: translate(-5px, -13px);
  &.mirrored {
    transform: translate(-5px, -13px) scaleX(-1);
  }
}
@keyframes dorian-dance {
  @for $i from 0 through 4 {
    #{beat-swing($i / 4) * 100}% { background-position: ($i * -33px) -94px; }
  }
}
/**
 * GOLDEN LUTE
 */
.golden-lute {
  width: 32px;
  height: 33px;
  background: $bgCharacters no-repeat;
  background-position: 0 -126px;
  animation: $beatTime step-end infinite golden-lute-dance;
  transform: translate(0, -29px);
}
@keyframes golden-lute-dance {
  @for $i from 0 through 4 {
    #{beat-swing($i / 4) * 100}% { background-position: ($i * -32px) -126px; }
  }
}
/**
 * THE NECRODANCER
 */
.necrodancer {
  width: 44px;
  height: 53px;
  background: $bgCharacters no-repeat;
  background-position: 0 0;
  animation: $beatTime step-end infinite necrodancer-dance;
  transform: translate(-11px, -36px);
  &.mirrored {
    transform: translate(-5px, -36px) scaleX(-1);
  }
}
@keyframes necrodancer-dance {
  @for $i from 0 through 4 {
    #{beat-swing($i / 4) * 100}% { background-position: ($i * -44px) 0; }
  }
}

[![Github Badge](https://img.shields.io/badge/-Diego%20Emanuel-6633cc?style=flat-square&logo=Github&logoColor=white&link=https://github.com/DiegoEmanuel/)](https://github.com/DiegoEmanuel/) 
[![Instagram Badge](https://img.shields.io/badge/-Diego%20Emanuel-6633cc?style=flat-square&logo=Instagram&logoColor=white&link=https://instagram.com/diego.efc/)](https://instagram.com/diego.efc/)  ...
</div>
<row>
<img src="https://raw.githubusercontent.com/Aniket965/Aniket965/master/pacman.svg?sanitize=true" width="35" height="35">
  
  <img src="https://raw.githubusercontent.com/Aniket965/Aniket965/master/pacman.svg?sanitize=true" width="35" height="35">
  </row>
today
// html 

// music embed in top-left
// click beating heart to turn on lights
input#lighting(type='checkbox',name='lighting')
label(for='lighting')
.lighting-status
input#info(type='checkbox',name='info')
label(for='info')
.info-overlay
  h2 from the game 
  a(href='http://store.steampowered.com/app/247080/',target='_blank')
    img(src='https://s3-us-west-2.amazonaws.com/s.cdpn.io/168886/necrodancer-header.png')
  h2 codepen by #[a(href='https://twitter.com/jhnsnc',target='_blank') Chris Johnson]
  p I'm just a fan of the game
  p I have no affiliation with the game or its creators
iframe.audio-embed(width=220,height=42,src='https://bandcamp.com/EmbeddedPlayer/album=441884888/size=small/bgcol=333333/linkcol=e99708/artwork=none/track=716340234/transparent=true/',seamless)
  a(href='http://dbsoundworks.bandcamp.com/album/crypt-of-the-necrodancer-ost') Crypt of the Necrodancer OST by Danny Baranowsky
.container
  .floor
    - for (var r=2;r<13;r+=1)
      - for (var c=0;c<17;c+=1)
        div(class='floor-tile unlit '+((r+c)%2?'odd':'even')+' pos-'+r+'-'+c)
        div(class='floor-tile lit '+((r+c)%2?'odd':'even')+' pos-'+r+'-'+c)
  .walls
    - for (var r=0;r<13;r+=1)
      - for (var c=0;c<17;c+=1)
        if (r===0 && c>3 && c<13) || (r===1 && (c<5 || c>11)) || ((r>1 && r<12) && (c===0 || c===16)) || (r===9 && c===8) || (r===12)
          div(class='wall-tile type-'+(Math.floor(1+Math.random()*5))+' pos-'+r+'-'+c+((c===2||c===10||(r===4&&c)||(r===8&&!c))?' torch-left':(c===6||c===14||(r===4&&!c)||(r===8&&c))?' torch-right':''))
  .stage
    - for (var r=2;r<4;r+=1)
      - for (var c=5;c<12;c+=1)
        if (r===2) || (r===3 && (c<7 || c>9))
          div(class='stage-tile type-'+(r===3?3:(c===5||c===11?4:5+c%2))+' pos-'+r+'-'+c)
  .characters
    .skeleton.pos-3-5
    .skeleton.pos-3-11
    .cadence.pos-7-6
    .dorian.mirrored.pos-8-10
    .golden-lute.pos-4-9
    .necrodancer.pos-5-6
