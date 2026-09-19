/**
 * ScrapCraft Studio - AI Smart Layout & Component Assistant
 */

let lastAiResponse = null;

async function requestAiLayoutSuggestion() {
  const promptInput = document.getElementById('ai-prompt-input');
  const prompt = promptInput ? promptInput.value.trim() : '';
  const resultPanel = document.getElementById('ai-results-panel');
  const loadingSpinner = document.getElementById('ai-loading-spinner');
  const btn = document.getElementById('btn-ai-generate');

  if (!prompt) {
    showToast('Vui lòng nhập ý tưởng bạn muốn (VD: kỷ niệm tốt nghiệp vintage, sinh nhật crush y2k...)', 'info');
    return;
  }

  if (loadingSpinner) loadingSpinner.classList.remove('hidden');
  if (btn) btn.disabled = true;

  try {
    const res = await fetch('/api/ai-suggest', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt: prompt })
    });

    const data = await res.json();
    lastAiResponse = data;

    if (data.status === 'success') {
      renderAiSuggestions(data);
      if (resultPanel) resultPanel.classList.remove('hidden');
      
      // Auto load preset into active canvas
      if (data.canvas_preset && typeof loadCanvasPreset === 'function') {
        loadCanvasPreset(data.canvas_preset);
      }
      
      showToast('✦ Memour AI: ' + (data.ai_reasoning || 'Đã bố trí bố cục & linh kiện tối ưu!'), 'success');
    } else {
      showToast('Không thể tạo gợi ý lúc này.', 'error');
    }
  } catch (err) {
    console.error('AI Error:', err);
    showToast('Lỗi kết nối máy chủ AI.', 'error');
  } finally {
    if (loadingSpinner) loadingSpinner.classList.add('hidden');
    if (btn) btn.disabled = false;
  }
}

function renderAiSuggestions(data) {
  const reasoningElem = document.getElementById('ai-reasoning-text');
  const itemsContainer = document.getElementById('ai-suggested-items');

  if (reasoningElem) {
    reasoningElem.innerText = data.ai_reasoning;
  }

  if (itemsContainer) {
    let items = [data.book, ...data.layouts, ...data.stickers];
    itemsContainer.innerHTML = items.map(item => `
      <div class="bg-white border border-black/20 rounded-xl p-2.5 flex items-center gap-2.5 shadow-sm hover:border-rose-700 transition-all">
        <img src="${item.image}" alt="${item.name}" loading="lazy" class="w-10 h-10 object-contain rounded bg-amber-50/50 p-1 border">
        <div class="flex-grow min-w-0">
          <div class="flex items-center gap-1.5">
            <span class="text-[10px] font-mono font-black bg-stone-900 text-white px-1.5 py-0.2 rounded">${item.sku}</span>
            <span class="text-[10px] text-stone-500 font-bold uppercase truncate">${item.category_name || item.category}</span>
          </div>
          <p class="text-xs font-bold text-stone-900 truncate">${item.name}</p>
        </div>
      </div>
    `).join('');
  }
}

function applyAiPresetToCanvas() {
  if (!lastAiResponse || !lastAiResponse.canvas_preset) {
    showToast('Chưa có dữ liệu gợi ý từ AI!', 'error');
    return;
  }

  loadCanvasPreset(lastAiResponse.canvas_preset);
  showToast('Đã áp dụng toàn bộ bố cục & linh kiện của AI lên Canvas!', 'success');
}

// Quick AI prompt buttons
function setAiPrompt(text) {
  const input = document.getElementById('ai-prompt-input');
  if (input) {
    input.value = text;
    requestAiLayoutSuggestion();
  }
}
