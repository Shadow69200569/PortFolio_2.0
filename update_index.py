import codecs
import re

with codecs.open('d:\\portfolio_2.0\\index.html', 'r', 'utf-8') as f:
    content = f.read()

# Replace the static code block
old_code_block = r'''            <div class="font-label-mono text-sm md:text-base leading-relaxed tracking-wide">
              <div class="text-tertiary">@RestController</div>
              <div class="text-tertiary">@RequestMapping<span class="text-text-low">("/api/v1")</span></div>
              <div class="text-accent-cyan mt-3">public class <span class="text-primary font-semibold">AiEngine</span> {</div>
              <div class="pl-6 mt-3 border-l-2 border-white/5">
                <div class="text-tertiary">@PostMapping<span class="text-text-low">("/predict")</span></div>
                <div class="text-accent-cyan">public <span class="text-white">Response</span> analyze(</div>
                <div class="pl-6 text-text-low">@RequestBody Data input</div>
                <div class="text-accent-cyan">) {</div>
                <div class="pl-6 text-primary mt-1 mb-1">return <span class="text-white">model.process(input);</span></div>
                <div class="text-accent-cyan">}</div>
              </div>
              <div class="text-accent-cyan mt-3">}</div>
            </div>'''

new_code_block = r'''            <div id="typewriter-code" class="font-label-mono text-sm md:text-base leading-relaxed tracking-wide min-h-[250px]">
              <!-- Typed.js will inject content here -->
            </div>'''

content = content.replace(old_code_block, new_code_block)

# Add Typed.js script before </body>
typed_script = r'''
<!-- Typed.js for Typewriter Effect -->
<script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>
<script>
  document.addEventListener('DOMContentLoaded', function() {
    var options = {
      strings: [
        <div class="text-tertiary">@RestController</div> +
        <div class="text-tertiary">@RequestMapping<span class="text-text-low">("/api/v1/quantum-core")</span></div> +
        <div class="text-accent-cyan mt-3">public class <span class="text-primary font-semibold">QuantumNeuralEngine</span> {</div> +
        <div class="pl-6 mt-3 border-l-2 border-white/5"> +
          <div class="text-tertiary">@PostMapping<span class="text-text-low">("/synthesize")</span></div> +
          <div class="text-accent-cyan">public <span class="text-white">NeuralResponse</span> synthesize(</div> +
          <div class="pl-6 text-text-low">@RequestBody ContextData input</div> +
          <div class="text-accent-cyan">) {</div> +
          <div class="pl-6 text-text-low mt-2 mb-1 opacity-50"># Initialize temporal embeddings</div> +
          <div class="pl-6 text-text-low mb-1">Tensor state = <span class="text-white">model.generate(input);</span></div> +
          <div class="pl-6 text-text-low mt-2 mb-1 opacity-50"># Execute multi-agent orchestration</div> +
          <div class="pl-6 text-primary mb-1">return <span class="text-white">agentMesh.orchestrate(state);</span></div> +
          <div class="text-accent-cyan">}</div> +
        </div> +
        <div class="text-accent-cyan mt-3">}</div>
      ],
      typeSpeed: 30,
      backSpeed: 0,
      loop: false,
      showCursor: true,
      cursorChar: '<span class="text-primary animate-pulse">|</span>',
      contentType: 'html'
    };

    var typed = new Typed('#typewriter-code', options);
  });
</script>
</body>'''

content = content.replace('</body>', typed_script)

with codecs.open('d:\\portfolio_2.0\\index.html', 'w', 'utf-8') as f:
    f.write(content)

print("Injected Typed.js into index.html")
