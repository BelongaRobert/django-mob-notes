const star = document.querySelector('#star-note')

star.addEventListener('click', function (e) {
  e.preventDefault()
  const starLink = e.currentTarget
  const starIcon = e.target
  const pk = starLink.dataset.pk

  fetch(starLink.href)
    .then(res => res.json())
    .then((data) => {
      if (data.note_starred) {
        starIcon.classList.replace('far', 'fas')
      } else {
        starIcon.classList.replace('fas', 'far')
      }
    })
})
