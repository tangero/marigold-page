---
title: "ChatGPT může používat některé aplikace na macOS pro efektivnější práci s kódem"
author: Patrick Zandl
post_excerpt: "ChatGPT pro macOS nyní nabízí možnost spolupracovat s vašimi aplikacemi, což přináší inteligentnější a přesnější odpovědi přizpůsobené vašim potřebám. V této rané beta verzi mohou uživatelé umožnit ChatGPT přístup k obsahu kódovacích aplikací, jako jsou Xcode, VS Code nebo TextEdit, pro lepší asistenci při vývoji."
layout: post
categories: [AI, OpenAI, ChatGPT]
thumbnail: https://venturebeat.com/wp-content/uploads/2020/04/openai-e1591041162109.jpg
---



ChatGPT pro macOS nyní nabízí možnost spolupracovat s vašimi aplikacemi. Kopíruje tím nedávno představenou funkci [Computer Use pro Claude](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) společnosti Anthropic. V beta verzi mohou uživatelé umožnit ChatGPT přístup k obsahu kódovacích aplikací, jako jsou Xcode, VS Code nebo TextEdit, pro lepší asistenci při vývoji. 

## Jak povolit práci s aplikacemi

Pro využití této funkce se ujistěte, že kompatibilní aplikace běží. V chatovacím okně ChatGPT klikněte na tlačítko “Práce s aplikacemi” a vyberte požadovanou aplikaci. Po výběru se nad vstupním polem zobrazí banner indikující, s jakými aplikacemi ChatGPT pracuje. Při odeslání zprávy bude ChatGPT zahrnovat obsah z těchto aplikací do svých odpovědí.

![Povolení ChatGPT apps](/assets/chatgpt-app.png)


Zahrnutý obsah \
- Editory a IDE (Xcode, VS Code, TextEdit): ChatGPT zahrne celý obsah otevřených editorů v popředním okně až do určitého limitu. Pokud v editoru vyberete konkrétní text, ChatGPT se zaměří na tento výběr, přičemž celý obsah panelu je stále použit jako kontext.
- Terminály (Terminal, iTerm): ChatGPT zahrne posledních 200 řádků z otevřených panelů. Pokud vyberete text v terminálu, ChatGPT se soustředí na tento výběr a přidá okolní text až do limitu.

Kompatibilní aplikace na vašem počítači můžete spravovat v Nastavení > Práce s aplikacemi > Spravovat aplikace.

V aplikaci následně stačí trojhmatem vyvolat okno ChatGPT a to může pracovat s textem v okně. Můžete třeba označit blok a požádat o opravu, doplnění, vysvětlení kódu. Mnoho jiného od toho zatím nečekejte. Zajímavá může být práce s Terminalem, kdy ChatGPT pobírá posledních 220 řádků příkazů a může za vás například komunikovat se serverem... 

![ChatGPT Editace článku ve VS Code](/assets/chatgpt-vscode-editace.png)

Tady je třeba vidět, jak jsem nechal do tohoto článku (edituji je ve VS Code) přidělat odstaveček o tom, jak se aplikace používá - ale nebojte, nepoužil jsem ho, napsal jsem si vlastní, protože je to strašně ukecaný. 

![Práce ve Visual Studio Code s podporou ChatGPT](/assets/chatgpt-prace-vsc.png)

A tady je vidět, jak to vypadá u programování ... 

## Technické aspekty

Pro umožnění této integrace využívá ChatGPT macOS Accessibility API k dotazování obsahu aplikací. Tuto funkci můžete kdykoli zakázat deaktivací přístupových oprávnění pro ChatGPT v nastavení systému. Pro spolupráci s VS Code je nutné nainstalovat speciální rozšíření, které umožňuje ChatGPT přístup k obsahu editoru.

## Ochrana dat a soukromí

Obsah z aplikací se stává součástí vaší historie chatu a je uložen ve vašem účtu, dokud jej nesmažete. Můžete ovládat, jak jsou vaše data používána:\
- Vylepšení modelu pro všechny: Můžete rozhodnout, zda vaše konverzace s ChatGPT mohou být použity k vylepšení modelů, přepnutím této volby v nastavení.
- Dočasné chaty: Pokud tuto funkci povolíte, vaše konverzace nebudou uloženy ani použity pro trénování modelů OpenAI.
- Další nastavení: Můžete exportovat své chaty nebo zcela smazat svůj účet.

Poznámka: U podnikových řešení, jako je ChatGPT Enterprise, není obsah použit pro vylepšení modelů. 


Integrace ChatGPT s aplikacemi na macOS představuje zajímavý krok vpřed v oblasti produktivity a efektivity při vývoji kódu. Je rozumné si vyzkoušet, jak vaši vývojářskou produktivitu takovéto propojení zvýší - a uvidíme, zda OpenAI bude v integraci s aplikacemi pokračovat, protože Computer Use s Claude toho umí přeci jen podstatně více, jenže je také zaměřený na integraci do aplikací a není tedy tak snadno použitelný pro koncového uživatele. Pro programátory a uživatele VS CODE je řešení ChatGPT velmi přímočaré... 

Navíc ChatGPT tím jde mírně proti Copilotu od partnerského Microsoftu. Čili uvidíme, co z toho všeho bude... 

Detailní [návod od OpenAI pro ChatGPT je zde](https://help.openai.com/en/articles/10119604-work-with-apps-on-macos). 