async function postData(url = '', data = {}) {
    // Default options are marked with *
    console.log("postData")
    console.log(JSON.stringify(data));
    const response = await fetch(url, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        headers: {
            'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return await response.json(); // parses JSON response into native JavaScript objects
}


let editor = new EditorJS({

    readOnly: false,

    holder: 'editorjs',

    /**
     * Common Inline Toolbar settings
     * - if true (or not specified), the order from 'tool' property will be used
     * - if an array of tool names, this order will be used
     */
    // inlineToolbar: ['link', 'marker', 'bold', 'italic'],
    // inlineToolbar: true,

    /**
     * Tools list
     */
    tools: {
        /**
         * Each Tool is a Plugin. Pass them via 'class' option with necessary settings {@link docs/tools.md}
         */
        header: {
            class: Header,
            inlineToolbar: ['marker', 'link'],
            config: {
                placeholder: 'Header'
            },
            shortcut: 'CMD+SHIFT+H'
        },

        /**
         * Or pass class directly without any configuration
         */
        image: SimpleImage,

        list: {
            class: List,
            inlineToolbar: true,
            shortcut: 'CMD+SHIFT+L'
        },

        checklist: {
            class: Checklist,
            inlineToolbar: true,
        },

        quote: {
            class: Quote,
            inlineToolbar: true,
            config: {
                quotePlaceholder: 'Enter a quote',
                captionPlaceholder: 'Quote\'s author',
            },
            shortcut: 'CMD+SHIFT+O'
        },

        warning: Warning,

        marker: {
            class: Marker,
            shortcut: 'CMD+SHIFT+M'
        },

        code: {
            class: CodeTool,
            shortcut: 'CMD+SHIFT+C'
        },

        delimiter: Delimiter,

        inlineCode: {
            class: InlineCode,
            shortcut: 'CMD+SHIFT+C'
        },

        linkTool: LinkTool,

        embed: Embed,

        table: {
            class: Table,
            inlineToolbar: true,
            shortcut: 'CMD+ALT+T'
        },

    },

    /**
     * This Tool will be used as default
     */
    defaultBlock: 'paragraph',

    i18n: {
        /**
         * @type {I18nDictionary}
         */
        messages: {
            /**
             * Other below: translation of different UI components of the editor.js core
             */
            ui: {
                "blockTunes": {
                    "toggler": {
                        "Click to tune": "Нажмите, чтобы настроить",
                        "or drag to move": "или перетащите"
                    },
                },
                "inlineToolbar": {
                    "converter": {
                        "Convert to": "Конвертировать в"
                    }
                },
                "toolbar": {
                    "toolbox": {
                        "Add": "Добавить"
                    }
                }
            },

            /**
             * Section for translation Tool Names: both block and inline tools
             */
            toolNames: {
                "Text": "Параграф",
                "Heading": "Заголовок",
                "List": "Список",
                "Warning": "Примечание",
                "Checklist": "Чеклист",
                "Quote": "Цитата",
                "Code": "Код",
                "Delimiter": "Разделитель",
                "Raw HTML": "HTML-фрагмент",
                "Table": "Таблица",
                "Link": "Ссылка",
                "Marker": "Маркер",
                "Bold": "Полужирный",
                "Italic": "Курсив",
                "InlineCode": "Моноширинный",
            },

            /**
             * Section for passing translations to the external tools classes
             */
            tools: {
                /**
                 * Each subsection is the i18n dictionary that will be passed to the corresponded plugin
                 * The name of a plugin should be equal the name you specify in the 'tool' section for that plugin
                 */
                "warning": { // <-- 'Warning' tool will accept this dictionary section
                    "Title": "Название",
                    "Message": "Сообщение",
                },

                /**
                 * Link is the internal Inline Tool
                 */
                "link": {
                    "Add a link": "Вставьте ссылку"
                },
                /**
                 * The "stub" is an internal block tool, used to fit blocks that does not have the corresponded plugin
                 */
                "stub": {
                    'The block can not be displayed correctly.': 'Блок не может быть отображен'
                }
            },

            /**
             * Section allows to translate Block Tunes
             */
            blockTunes: {
                /**
                 * Each subsection is the i18n dictionary that will be passed to the corresponded Block Tune plugin
                 * The name of a plugin should be equal the name you specify in the 'tunes' section for that plugin
                 *
                 * Also, there are few internal block tunes: "delete", "moveUp" and "moveDown"
                 */
                "delete": {
                    "Delete": "Удалить"
                },
                "moveUp": {
                    "Move up": "Переместить вверх"
                },
                "moveDown": {
                    "Move down": "Переместить вниз"
                }
            },
        }
    },

    /**
     * Initial Editor data
     */
    data: {
        {{ data['blocks'] }}
    },
    onReady: function () {
        saveButton.click();
    },
    onChange: function () {
        console.log('something changed');
    }
});

/**
 * Saving button
 */
const saveButton = document.getElementById('saveButton');

/**
 * Toggle read-only button
 */
const toggleReadOnlyButton = document.getElementById('toggleReadOnlyButton');
const readOnlyIndicator = document.getElementById('readonly-state');

/**
 * Saving example
 */
saveButton.addEventListener('click', function () {
    editor.save().then((outputData) => {
        console.log(outputData);
        postData('/articles/new', outputData).then((data) => {
            console.log(data); // JSON data parsed by `response.json()` call
        });
    }).catch((error) => {
        console.log('Saving failed: ', error)
    });
});


/**
 * Toggle read-only example
 */
toggleReadOnlyButton.addEventListener('click', async () => {
    const readOnlyState = await editor.readOnly.toggle();

    readOnlyIndicator.textContent = readOnlyState ? 'On' : 'Off';
});
