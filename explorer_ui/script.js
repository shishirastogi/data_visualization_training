let currentPath = '';

const folderSVG = `
<svg viewBox="0 0 100 80" width="70" height="70">
    <path class="svg-folder" d="M5 25 L5 75 L95 75 L95 25 Z" />
    <path class="svg-folder" d="M5 25 L5 15 C5 10, 10 5, 15 5 L35 5 C40 5, 45 10, 50 15 L95 15 L95 25 Z" />
</svg>
`;

const fileSVG = `
<svg viewBox="0 0 70 90" width="60" height="70">
    <path class="svg-file" d="M5 5 L45 5 L65 25 L65 85 L5 85 Z" />
    <path class="svg-file" d="M45 5 L45 25 L65 25" />
    <circle cx="25" cy="45" r="3.5" fill="#1A1A1A" />
    <circle cx="45" cy="45" r="3.5" fill="#1A1A1A" />
    <path d="M 25 60 Q 35 70 45 60" fill="none" stroke="#1A1A1A" stroke-width="2.5" stroke-linecap="round" />
</svg>
`;

const fileGrid = document.getElementById('file-grid');
const pathDisplay = document.getElementById('path-display');
const btnUp = document.getElementById('btn-up');

const fileModal = document.getElementById('file-modal');
const modalClose = document.getElementById('modal-close');
const modalOk = document.getElementById('modal-ok');
const modalTitle = document.getElementById('modal-title');
const fileContent = document.getElementById('file-content');

async function loadDirectory(dirPath) {
    try {
        const response = await fetch(`/api/files?dir=${encodeURIComponent(dirPath)}`);
        if (!response.ok) throw new Error('Failed to fetch directory');
        
        const files = await response.json();
        currentPath = dirPath;
        pathDisplay.innerText = '/' + currentPath;
        
        renderFiles(files);
    } catch (error) {
        alert("Error loading directory: " + error.message);
    }
}

function renderFiles(files) {
    fileGrid.innerHTML = '';
    
    files.forEach(file => {
        const item = document.createElement('div');
        item.className = 'item';
        
        const icon = document.createElement('div');
        icon.className = 'item-icon';
        icon.innerHTML = file.type === 'directory' ? folderSVG : fileSVG;
        
        const label = document.createElement('div');
        label.className = 'item-label';
        label.innerText = file.name;
        
        item.appendChild(icon);
        item.appendChild(label);
        
        item.addEventListener('dblclick', () => {
            if (file.name === '..') {
                loadDirectory(file.path);
            } else if (file.type === 'directory') {
                loadDirectory(file.path);
            } else {
                openFile(file.path, file.name);
            }
        });
        
        fileGrid.appendChild(item);
    });
}

async function openFile(filePath, fileName) {
    try {
        const response = await fetch(`/api/file_content?file=${encodeURIComponent(filePath)}`);
        if (!response.ok) {
            // For binary files, just show a message or download it.
            // Since this is a simple text explorer, we'll try to read it anyway, or fail.
            throw new Error('Failed to fetch file content or file is binary');
        }
        
        const content = await response.text();
        modalTitle.innerText = fileName;
        fileContent.value = content;
        fileModal.classList.remove('hidden');
    } catch (error) {
        alert("Cannot preview this file: " + error.message);
    }
}

btnUp.addEventListener('click', () => {
    if (currentPath === '') return;
    const parts = currentPath.split('/');
    parts.pop();
    loadDirectory(parts.join('/'));
});

modalClose.addEventListener('click', () => fileModal.classList.add('hidden'));
modalOk.addEventListener('click', () => fileModal.classList.add('hidden'));

// Initial load
loadDirectory('');
