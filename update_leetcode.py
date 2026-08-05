import re

# Read github.html for the shell
with open('d:/portfolio_2.0/github.html', 'r', encoding='utf-8') as f:
    github_content = f.read()

# Extract header + nav + opening main tag
# The <main ...> tag in github.html
main_start_match = re.search(r'(<main[^>]*>)', github_content)
if not main_start_match:
    print("Could not find <main> in github.html")
    exit(1)

shell_top = github_content[:main_start_match.end()]

# Extract footer + closing tags
main_end_match = re.search(r'(</main>)', github_content)
if not main_end_match:
    print("Could not find </main> in github.html")
    exit(1)

shell_bottom = github_content[main_end_match.start():]

# We also need to change the page title and description
shell_top = shell_top.replace('<title>Sandeep | GitHub Dashboard</title>', '<title>Sandeep | LeetCode Dashboard</title>')
shell_top = shell_top.replace('<meta name="description" content="Live GitHub activity dashboard — real repos, contributions and activity for Shadow69200569."/>', '<meta name="description" content="Live LeetCode activity dashboard — real stats, difficulties and recent submissions."/>')
shell_top = shell_top.replace('id="gh-profile-link" href="https://github.com/Shadow69200569"', 'id="lc-profile-link" href="https://leetcode.com/u/08E4aDwjHC/"')

# Now let's build the main content for LeetCode
main_content = """
  <!-- ── Profile Header ── -->
  <section class="reveal d1 glass-card rounded-3xl p-card-padding flex flex-col md:flex-row items-center gap-8 md:gap-12 relative overflow-hidden">
    <div class="blob w-64 h-64 bg-accent-orange/20 top-0 left-0"></div>
    <div class="relative w-32 h-32 md:w-48 md:h-48 flex-shrink-0">
      <div class="absolute inset-0 rounded-full border border-glass-border"></div>
      <img src="https://assets.leetcode.com/users/08E4aDwjHC/avatar_1736690500.png" alt="Sandeep LeetCode Avatar" class="w-full h-full rounded-full object-cover relative z-10 p-2">
      <div class="absolute inset-0 rounded-full border-[2px] border-transparent border-t-accent-cyan/50 border-r-accent-cyan/50 animate-spin-slow"></div>
    </div>
    <div class="flex-1 text-center md:text-left z-10">
      <h1 class="font-headline-lg text-headline-lg-mobile md:text-headline-lg text-text-high mb-2 tracking-tight">Sandeep</h1>
      <p class="font-body-lg text-body-lg text-text-low mb-6 max-w-2xl">
        Level 42 Architect <span class="text-accent-cyan">@LeetCode</span>
      </p>
      <div class="flex flex-wrap justify-center md:justify-start gap-3">
        <a href="https://leetcode.com/u/08E4aDwjHC/" target="_blank" rel="noopener" class="px-6 py-2 rounded-full border border-glass-border text-text-high hover:bg-white/5 transition-all text-sm font-semibold flex items-center gap-2">
          View Profile <span class="material-symbols-outlined text-[18px]">open_in_new</span>
        </a>
      </div>
    </div>
  </section>

  <!-- ── Stats Overview ── -->
  <section class="reveal d2 grid grid-cols-2 md:grid-cols-4 gap-4">
    <div class="glass-card rounded-2xl p-6 flex flex-col items-center justify-center text-center group">
      <span class="material-symbols-outlined text-accent-cyan text-3xl mb-3 group-hover:scale-110 transition-transform">task_alt</span>
      <span class="font-headline-md text-3xl font-bold text-text-high mb-1" id="total-solved-text">0</span>
      <span class="font-body-md text-text-low text-sm">Total Solved</span>
    </div>
    <div class="glass-card rounded-2xl p-6 flex flex-col items-center justify-center text-center group">
      <span class="material-symbols-outlined text-accent-orange text-3xl mb-3 group-hover:scale-110 transition-transform">trophy</span>
      <span class="font-headline-md text-3xl font-bold text-text-high mb-1" id="global-rank-text">0</span>
      <span class="font-body-md text-text-low text-sm">Global Rank</span>
    </div>
    <div class="glass-card rounded-2xl p-6 flex flex-col items-center justify-center text-center group">
      <span class="material-symbols-outlined text-green-400 text-3xl mb-3 group-hover:scale-110 transition-transform">check_circle</span>
      <span class="font-headline-md text-3xl font-bold text-green-400 mb-1" id="ac-submissions-text">0</span>
      <span class="font-body-md text-text-low text-sm">Total Submissions</span>
    </div>
    <div class="glass-card rounded-2xl p-6 flex flex-col items-center justify-center text-center group">
      <span class="material-symbols-outlined text-secondary text-3xl mb-3 group-hover:scale-110 transition-transform">stars</span>
      <span class="font-headline-md text-3xl font-bold text-secondary mb-1">Actv</span>
      <span class="font-body-md text-text-low text-sm">Status</span>
    </div>
  </section>

  <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
    <!-- ── Left Column: Recent Submissions ── -->
    <div class="lg:col-span-2 flex flex-col gap-6">
      <section class="reveal d3 glass-card rounded-2xl p-6 md:p-8 flex-1">
        <div class="flex justify-between items-center mb-6">
          <h2 class="font-headline-md text-2xl text-text-high flex items-center gap-2">
            <span class="material-symbols-outlined text-accent-orange">history</span> Recent Submissions
          </h2>
        </div>
        <div class="flex flex-col gap-2" id="recent-submissions-container">
          <div class="grid grid-cols-12 gap-4 px-4 py-2 border-b border-glass-border/50 text-text-low text-sm">
            <div class="col-span-8">Problem</div>
            <div class="col-span-4 text-right">Time</div>
          </div>
          <div id="submissions-list">
              <!-- JS Injected rows will go here -->
              <div class="p-8 text-center text-text-low skeleton">Loading submissions...</div>
          </div>
        </div>
      </section>
    </div>

    <!-- ── Right Column: Difficulty Breakdown ── -->
    <div class="flex flex-col gap-6">
      <section class="reveal d3 glass-card rounded-2xl p-6 md:p-8 hover:border-glass-border/50 transition-colors">
        <h2 class="font-headline-md text-xl text-text-high mb-6 flex items-center gap-2">
          <span class="material-symbols-outlined text-accent-cyan">donut_large</span> Difficulty Breakdown
        </h2>
        
        <div class="flex flex-col gap-6">
          <!-- Easy -->
          <div class="flex items-center gap-4">
            <div class="relative w-16 h-16 flex-shrink-0">
              <svg class="w-full h-full -rotate-90" viewbox="0 0 100 100">
                <circle cx="50" cy="50" fill="transparent" r="40" stroke="rgba(255,255,255,0.1)" stroke-width="8"></circle>
                <circle id="easy-circle" class="transition-all duration-1000" cx="50" cy="50" fill="transparent" r="40" stroke="#4ade80" stroke-width="8" style="stroke-dasharray: 251.2; stroke-dashoffset: 251.2;"></circle>
              </svg>
              <div id="easy-count" class="absolute inset-0 flex items-center justify-center text-text-high text-sm font-bold">0</div>
            </div>
            <div class="flex-1">
              <div class="flex justify-between mb-2">
                <span class="text-text-high font-medium">Easy</span>
                <span id="easy-percentage" class="text-text-low text-sm">0%</span>
              </div>
              <div class="w-full h-2 bg-white/5 rounded-full overflow-hidden">
                <div id="easy-bar" class="h-full bg-[#4ade80] rounded-full transition-all duration-1000" style="width: 0%"></div>
              </div>
            </div>
          </div>
          <!-- Medium -->
          <div class="flex items-center gap-4">
            <div class="relative w-16 h-16 flex-shrink-0">
              <svg class="w-full h-full -rotate-90" viewbox="0 0 100 100">
                <circle cx="50" cy="50" fill="transparent" r="40" stroke="rgba(255,255,255,0.1)" stroke-width="8"></circle>
                <circle id="medium-circle" class="transition-all duration-1000" cx="50" cy="50" fill="transparent" r="40" stroke="#facc15" stroke-width="8" style="stroke-dasharray: 251.2; stroke-dashoffset: 251.2;"></circle>
              </svg>
              <div id="medium-count" class="absolute inset-0 flex items-center justify-center text-text-high text-sm font-bold">0</div>
            </div>
            <div class="flex-1">
              <div class="flex justify-between mb-2">
                <span class="text-text-high font-medium">Medium</span>
                <span id="medium-percentage" class="text-text-low text-sm">0%</span>
              </div>
              <div class="w-full h-2 bg-white/5 rounded-full overflow-hidden">
                <div id="medium-bar" class="h-full bg-[#facc15] rounded-full transition-all duration-1000" style="width: 0%"></div>
              </div>
            </div>
          </div>
          <!-- Hard -->
          <div class="flex items-center gap-4">
            <div class="relative w-16 h-16 flex-shrink-0">
              <svg class="w-full h-full -rotate-90" viewbox="0 0 100 100">
                <circle cx="50" cy="50" fill="transparent" r="40" stroke="rgba(255,255,255,0.1)" stroke-width="8"></circle>
                <circle id="hard-circle" class="transition-all duration-1000" cx="50" cy="50" fill="transparent" r="40" stroke="#f87171" stroke-width="8" style="stroke-dasharray: 251.2; stroke-dashoffset: 251.2;"></circle>
              </svg>
              <div id="hard-count" class="absolute inset-0 flex items-center justify-center text-text-high text-sm font-bold">0</div>
            </div>
            <div class="flex-1">
              <div class="flex justify-between mb-2">
                <span class="text-text-high font-medium">Hard</span>
                <span id="hard-percentage" class="text-text-low text-sm">0%</span>
              </div>
              <div class="w-full h-2 bg-white/5 rounded-full overflow-hidden">
                <div id="hard-bar" class="h-full bg-[#f87171] rounded-full transition-all duration-1000" style="width: 0%"></div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
"""

js_content = """
<script>
  // Setup reveal observer
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
      }
    });
  }, { threshold: 0.1 });
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

  // Mobile menu toggle
  const mobBtn = document.getElementById('mob-btn');
  const mobMenu = document.getElementById('mob-menu');
  if(mobBtn && mobMenu) {
    mobBtn.addEventListener('click', () => {
      mobMenu.classList.toggle('hidden');
      mobMenu.classList.toggle('flex');
    });
  }

  // LeetCode API Integration
  const username = '08E4aDwjHC';
  const profileApi = `https://alfa-leetcode-api.onrender.com/${username}`;
  const solvedApi = `https://alfa-leetcode-api.onrender.com/${username}/solved`;
  const submissionsApi = `https://alfa-leetcode-api.onrender.com/${username}/acSubmission`;

  async function fetchLeetCodeData() {
      try {
          const [profileRes, solvedRes, subRes] = await Promise.all([
              fetch(profileApi),
              fetch(solvedApi),
              fetch(submissionsApi)
          ]);
          
          const profileData = await profileRes.json();
          const solvedData = await solvedRes.json();
          const subData = await subRes.json();

          updateDashboard(profileData, solvedData, subData);
      } catch (error) {
          console.error("Error fetching LeetCode data:", error);
          document.getElementById('submissions-list').innerHTML = '<div class="p-8 text-center text-red-400">Failed to load data. Please try again later.</div>';
      }
  }

  function updateDashboard(profile, stats, submissions) {
      // Stats
      document.getElementById('total-solved-text').innerText = stats.solvedProblem || 0;
      document.getElementById('global-rank-text').innerText = (profile.ranking || 0).toLocaleString();
      
      const totalSub = stats.totalSubmissionNum?.find(s => s.difficulty === 'All')?.submissions || 0;
      document.getElementById('ac-submissions-text').innerText = totalSub.toLocaleString();

      // Difficulties
      const totalSolved = stats.solvedProblem || 1; // Prevent div by zero
      
      const diffs = [
          { name: 'easy', count: stats.easySolved || 0 },
          { name: 'medium', count: stats.mediumSolved || 0 },
          { name: 'hard', count: stats.hardSolved || 0 }
      ];

      diffs.forEach(diff => {
          const percent = Math.round((diff.count / totalSolved) * 100) || 0;
          document.getElementById(`${diff.name}-count`).innerText = diff.count;
          document.getElementById(`${diff.name}-percentage`).innerText = `${percent}%`;
          document.getElementById(`${diff.name}-bar`).style.width = `${percent}%`;
          
          // Circle offset logic
          const circum = 251.2;
          const offset = circum - (percent / 100) * circum;
          document.getElementById(`${diff.name}-circle`).style.strokeDashoffset = offset;
      });

      // Submissions
      const subList = document.getElementById('submissions-list');
      subList.innerHTML = ''; // clear loading state
      
      if (submissions && submissions.submission && submissions.submission.length > 0) {
          const top10 = submissions.submission.slice(0, 10);
          top10.forEach(sub => {
              const date = new Date(sub.timestamp * 1000);
              const now = new Date();
              const diffMs = now - date;
              const diffMins = Math.floor(diffMs / 60000);
              const diffHrs = Math.floor(diffMins / 60);
              const diffDays = Math.floor(diffHrs / 24);
              let timeStr = '';
              if (diffDays > 0) timeStr = `${diffDays} days ago`;
              else if (diffHrs > 0) timeStr = `${diffHrs} hrs ago`;
              else timeStr = `${diffMins} mins ago`;

              const row = document.createElement('a');
              row.href = `https://leetcode.com/problems/${sub.titleSlug}/`;
              row.target = "_blank";
              row.className = 'grid grid-cols-12 gap-4 px-4 py-3 bg-white/5 rounded-lg hover:bg-white/10 transition-colors items-center group mb-2 border border-glass-border/50';
              
              row.innerHTML = `
                  <div class="col-span-8 font-body-md text-text-high flex items-center gap-3 truncate">
                      <span class="material-symbols-outlined text-green-400 text-[18px]">check_circle</span>
                      <span class="group-hover:text-accent-cyan transition-colors truncate">${sub.title}</span>
                  </div>
                  <div class="col-span-4 text-right font-label-sm text-text-low text-sm">${timeStr}</div>
              `;
              subList.appendChild(row);
          });
      } else {
          subList.innerHTML = '<div class="p-8 text-center text-text-low">No recent submissions found.</div>';
      }
  }

  // Initialize
  fetchLeetCodeData();
</script>
"""

final_content = shell_top + main_content + shell_bottom.replace('</body>', js_content + '</body>')

with open('d:/portfolio_2.0/leetcode.html', 'w', encoding='utf-8') as f:
    f.write(final_content)
    
print("Successfully generated new leetcode.html")
