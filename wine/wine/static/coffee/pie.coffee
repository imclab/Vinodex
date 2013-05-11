PIE_RADIUS = 200
WIDTH = 800
HEIGHT = 500

renderPie = (div, dataset, displaySettings = {}) ->
  radius = displaySettings.radius or PIE_RADIUS
  width = displaySettings.width or WIDTH
  height = displaySettings.height or HEIGHT

  color = d3.scale.category20()

  pie = d3.layout.pie()
          .sort(null)
          .value((d) -> d.value)

  arc = d3.svg.arc().outerRadius(radius)

  svg = d3.select(div)
          .append("svg")
          .attr("width", width)
          .attr("height", height)
          .attr("transform", "translate(#{width / 2}, #{height / 2})")

  path = svg.selectAll("path")
            .data(pie(dataset))
            .enter().append("path")
            .attr("fill", (d, i) -> color(i))
            .attr("d", arc)
            .each((d) -> this._current = d )

  labelGroup = svg.append("g")
              .attr("class", "lblGroup")
              .attr("transform", "translate(#{width / 2}, #{height / 2})")

  label = labelGroup.selectAll("text")
                    .data(pie(dataset))
  
  label.enter()
       .append("text")
       .attr("class", "arcLabel")
       .attr("transform", (d) -> "translate(#{arc.centroid(d)})")
       .attr("text-anchor", "middle")
       .style("fill-opacity", (d) ->
          if d.value == 0 then 1e-6 else 1
        )
       .text((d) -> d.data.label)

$ ->
  dataset = [{label: "I", value: 1},
             {label: "Like", value: 2},
             {label: "Pie", value: 3},
             {label: "Charts", value: 4}]
  renderPie("body",dataset)


