using System.Text.Json;
using ChecklistGenerator.Models;
using Microsoft.JSInterop;

namespace ChecklistGenerator.Services
{
    public class ChecklistService
    {
        private readonly IJSRuntime _js;
        private const string StorageKey = "checklists";

        public List<Checklist> Lists { get; private set; } = new();

        public ChecklistService(IJSRuntime js)
        {
            _js = js;
        }

        public async Task LoadAsync()
        {
            var json = await _js.InvokeAsync<string>("localStorage.getItem", StorageKey);
            if (!string.IsNullOrEmpty(json))
            {
                var data = JsonSerializer.Deserialize<List<Checklist>>(json);
                if (data != null)
                {
                    Lists = data;
                }
            }
        }

        private async Task SaveAsync()
        {
            var json = JsonSerializer.Serialize(Lists);
            await _js.InvokeVoidAsync("localStorage.setItem", StorageKey, json);
        }

        public async Task AddChecklist(Checklist checklist)
        {
            Lists.Add(checklist);
            await SaveAsync();
        }

        public async Task UpdateChecklist(Checklist checklist)
        {
            await SaveAsync();
        }

        public async Task DeleteChecklist(Checklist checklist)
        {
            Lists.Remove(checklist);
            await SaveAsync();
        }
    }
}
