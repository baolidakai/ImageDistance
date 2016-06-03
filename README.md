<h1>Image Distance Metric Study</h1>

<hr />

<p>
Steps:
<ol>
<li>Resize two images onto the same scale</li>
<li>Get patches of these images (e.g. 5x5)</li>
<li>Compute the Euclidean distance of all different patches (might be expensive)</li>
<li>Get the minimum cost perfect matching with an efficient algorithm (Hungarian's algorithm e.g.)</li>
<li>Compute simulated image distance (e.g. Very similar images, very dissimilar images)</li>
</ol>
</p>
