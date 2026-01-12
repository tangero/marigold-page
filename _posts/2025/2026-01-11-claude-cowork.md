---
author: Patrick Zandl
categories:
- AI
- Anthropic
- Claude
- agenti
layout: post
post_excerpt: Anthropic spustil Cowork, nástroj pro automatizaci kancelářské práce postavený na Claude Agent SDK. Zatím pouze pro předplatitele Claude Max na macOS.
summary_points:
- Cowork přináší agentní schopnosti Claude Code běžným uživatelům bez nutnosti práce s terminálem
- Nástroj umožňuje Claude číst, upravovat a vytvářet soubory ve vybrané složce na počítači
- K dispozici pouze pro předplatitele Claude Max na macOS, ostatní se mohou zapsat na čekací seznam
- Bezpečnostní rizika zahrnují možnost prompt injection útoků a destruktivních akcí
- Cowork lze kombinovat s konektory pro Gmail nebo Google Drive a s prohlížečovým agentem Claude in Chrome
title: Anthropic představil Cowork, Claude Code pro ty ostatní...
---

Anthropic 12. ledna 2026 spustil [Cowork](https://claude.com/blog/cowork), novou funkci integrovanou do desktopové aplikace Claude pro macOS. Cowork zpřístupňuje agentní schopnosti Claude Code širšímu okruhu uživatelů bez nutnosti pracovat s příkazovou řádkou nebo nastavovat vývojářské prostředí. Nástroj je zatím dostupný pouze pro předplatitele tarifu Claude Max jako takzvaný výzkumný náhled.

## Jak Cowork funguje

Princip Cowork je přímočarý. Uživatel vybere konkrétní složku na svém počítači, ke které Claude získá přístup. V rámci této složky může asistent číst existující soubory, upravovat je nebo vytvářet nové. Komunikace probíhá přes standardní chatové rozhraní v desktopové aplikaci Claude.

Praktické využití zahrnuje organizaci souborů ve složce Stažené, vytvoření tabulky výdajů z hromady snímků obrazovky s účtenkami nebo sepsání první verze zprávy z roztříštěných poznámek. Po zadání úkolu Claude vytvoří plán a samostatně ho realizuje, přičemž uživatele průběžně informuje o postupu. Na rozdíl od běžné konverzace s chatbotem zde model pracuje s mnohem větší mírou autonomie.

Technicky je Cowork postaven na stejných základech jako Claude Code. Konkrétně využívá Claude Agent SDK, sadu nástrojů původně vyvinutou pro programátorský nástroj Claude Code a nyní přejmenovanou tak, aby lépe odrážela širší využití. SDK poskytuje automatickou správu kontextu, vestavěné nástroje pro práci se soubory a spouštění příkazů, podporu MCP serverů pro rozšíření funkcionality a mechanismy pro řízení oprávnění.

## Rozšířené možnosti s konektory a dovednostmi

Cowork lze propojit s existujícími konektory Claude, které zajišťují přístup k externím službám jako Gmail nebo Google Drive. Anthropic také přidal sadu takzvaných dovedností (Skills), které zlepšují schopnost Claude vytvářet dokumenty, prezentace a další typy souborů. Tyto dovednosti jsou modulární balíčky instrukcí uložené ve formátu SKILL.md, které Claude automaticky aktivuje, když jsou relevantní pro daný úkol.

Pro uživatele, kteří mají nainstalované rozšíření [Claude in Chrome](https://claude.com/chrome), přibývá možnost zadávat úkoly vyžadující práci v prohlížeči. Agent tak může například vyhledat informace na webu a následně je zpracovat do požadovaného formátu ve složce.

Významnou vlastností je možnost řazení úkolů do fronty. Uživatel nemusí čekat na dokončení jednoho úkolu, než zadá další. Claude zpracovává požadavky paralelně, což podle Anthropic připomíná spíše zanechávání zpráv kolegovi než klasickou konverzaci tam a zpět.

## Bezpečnostní omezení a rizika

Anthropic v oznámení věnuje značný prostor bezpečnostním aspektům. Uživatel má plnou kontrolu nad tím, ke kterým složkám a konektorům Claude přistupuje. Model si před provedením významných akcí vyžádá souhlas, což umožňuje průběžnou korekci směru práce.

Existují však rizika, která nelze zcela eliminovat. Claude může při chybné interpretaci instrukcí provést destruktivní akce, například smazat soubory. Anthropic doporučuje formulovat pokyny co nejpřesněji, zejména u operací, které mohou způsobit nevratné změny.

Druhým významným rizikem jsou takzvané prompt injection útoky. Jedná se o techniku, kdy útočník vloží do obsahu, se kterým Claude pracuje, instrukce, které změní chování agenta. Anthropic implementoval obranné mechanismy, ale přiznává, že zabezpečení agentních systémů zůstává aktivní oblastí vývoje v celém odvětví. Podrobnější informace o bezpečném používání firma zveřejnila v [nápovědě](https://support.claude.com/en/articles/13364135-using-cowork-safely).

## Dostupnost a cena

|Parametr               |Hodnota                                                          |
|-----------------------|-----------------------------------------------------------------|
|Platforma              |macOS (desktopová aplikace Claude)                               |
|Požadovaný tarif       |Claude Max                                                       |
|Cena tarifu Max        |100 USD/měsíc (5× limity Pro) nebo 200 USD/měsíc (20× limity Pro)|
|Fáze                   |Výzkumný náhled                                                  |
|Alternativa pro ostatní|[Čekací seznam](https://forms.gle/mtoJrd8kfYny29jQ9)             |

Claude Max je prémiový tarif Anthropic určený pro intenzivní uživatele. Za 100 dolarů měsíčně poskytuje pětinásobek využití oproti tarifu Pro, varianta za 200 dolarů pak dvacetinásobek. Tarif zahrnuje přístup k nejnovějším modelům včetně Claude Opus 4.5 a přednostní přístup k novým funkcím.

Pro uživatele Windows zatím Cowork není dostupný. Anthropic plánuje rozšíření platformové podpory i přidání synchronizace mezi zařízeními, konkrétní termíny však nezveřejnil.

## Kontext a konkurence

Vznik Cowork není náhodný. Claude Code se během posledního roku stal jedním z nejúspěšnějších produktů Anthropic a uživatelé ho začali využívat daleko za hranicemi programování. Nástroj původně určený vývojářům našel uplatnění při výzkumu, zpracování dokumentů nebo automatizaci administrativních úkolů. Cowork je reakcí na tento organický vývoj a pokusem zpřístupnit agentní schopnosti širšímu publiku.

V širším kontextu jde o součást trendu, kdy hlavní poskytovatelé AI řešení posouvají své produkty směrem k autonomním agentům schopným vykonávat komplexní úkoly bez průběžného dohledu. Otázkou zůstává, zda a jak rychle se tyto nástroje skutečně prosadí v běžné kancelářské práci. Dosavadní data o produktivitě AI nástrojů v pracovním prostředí jsou rozporuplná a mnoho organizací stále bojuje se smysluplnou integrací.​​​​​​​​​​​​​​​​