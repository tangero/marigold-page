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
thumbnail: https://www.marigold.cz/assets/claude-cowork.png
---

Anthropic 12. ledna 2026 spustil [Cowork](https://claude.com/blog/cowork), novou funkci integrovanou do desktopové aplikace Claude pro macOS. Cowork zpřístupňuje agentní schopnosti Claude Code širšímu okruhu uživatelů bez nutnosti pracovat s příkazovou řádkou nebo nastavovat vývojářské prostředí. Nástroj je zatím dostupný pouze pro předplatitele tarifu Claude Max jako "výzkumný náhled". Jak funguje a máte se na něj těšit? 

## Jak Cowork funguje

Princip Cowork je přímočarý. Uživatel vybere konkrétní složku na svém počítači, ke které Claude získá přístup. Proto také vázanost na MacOS - používá se jeho sandboxing, čili z vyhražené složky Cowork bez vašeho souhlasu "nevyleze".  V rámci této složky může asistent číst existující soubory, upravovat je nebo vytvářet nové. Komunikace probíhá přes standardní chatové rozhraní v desktopové aplikaci Claude. Jak to vypadá, vidíte na obrázku, kde jsem Cowork pověřil, aby mi uklidil pracovní plochu. Zvládl to moc dobře :)

![Takhle vypadá Claude Cowork](/assets/images/claude-cowork.png)

Architektura Cowork staví na několika základních komponentách. Konektory a MCP servery zajišťují přístup k externím službám jako Gmail nebo Google Kalendář. Přístup k souborovému systému umožňuje vytváření a čtení lokálních souborů. Systém kroků (TODOs/Steps) zobrazuje diskrétní sledovatelné kroky, které Cowork provádí při plnění úkolu. Artefakty představují soubory vygenerované během práce a kontextová sekce ukazuje soubory, zdroje a konektory použité při zpracování. Součástí jsou také předinstalované dovednosti (Skills), zejména pro vytváření souborů jako DOCX nebo PPTX.

Praktické využití zahrnuje organizaci souborů ve složce Stažené, vytvoření tabulky výdajů z hromady snímků obrazovky s účtenkami nebo sepsání první verze zprávy z roztříštěných poznámek. Po zadání úkolu Claude vytvoří plán a samostatně ho realizuje, přičemž uživatele průběžně informuje o postupu. Na rozdíl od běžné konverzace s chatbotem zde model pracuje s mnohem větší mírou autonomie. Ale když jsem ho pověřil, aby mi vytahal z konkrétních emailů od konkrétních lidí PDF soubory a ty zpracoval, tak prostě některé soubory pominul, ačkoliv se tvářil, že na tom usilovně dřel...

Technicky je Cowork postaven na stejných základech jako Claude Code. Konkrétně využívá Claude Agent SDK, sadu nástrojů původně vyvinutou pro programátorský nástroj Claude Code a nyní přejmenovanou tak, aby lépe odrážela širší využití. SDK poskytuje automatickou správu kontextu, vestavěné nástroje pro práci se soubory a spouštění příkazů, podporu MCP serverů pro rozšíření funkcionality a mechanismy pro řízení oprávnění.

## Startovací úkoly a uživatelské rozhraní

Rozhraní Cowork nabízí sadu předpřipravených startovacích úkolů, které naznačují zamýšlené použití nástroje. Patří mezi ně vytvoření souboru, analýza dat, vytvoření prototypu, příprava na den s analýzou kalendáře nebo napsání zprávy pro sociální sítě, e-mail či kolegy.

Startovací úkoly používají přístup podobný doplňování šablony, kde uživatel vyplňuje parametry do předpřipraveného promptu. Tato metoda je přístupnější než psaní instrukcí od nuly, i když zkušenější uživatelé nemusí pociťovat významný rozdíl oproti přímému zadávání v běžném chatu.

Sám jsem si hned přidal své projektové plánování založené na tom, že si zkládám dokumenty k projektům a zápisy z porad a pomocí přednastavených Skillů je stále do kolečka analyzuju typu "jaké vznikly úkoly a co je potřeba udělat dále". Jenže se hned ukázala nevýhoda: soubory musíte přetahovat do souborového systému, nemůžete je přesunout do aplikace Claude, protože tam není kam. Když jste v Projektu u aplikace Claude (který v Coworku nefunguje), tak tam si soubor nahrajete do knihovny a dále s ním pracujete. Tady jej musíte zkopírovat přes souborový systém do adresáře na disku. 

## Rozšířené možnosti s konektory a dovednostmi

Cowork lze propojit s existujícími konektory Claude, které zajišťují přístup k externím službám jako Gmail nebo Google Drive - a tak dvou desítek dalších konektorů včetně třeba Stripe nebo GitHub. Anthropic také přidal sadu takzvaných dovedností (Skills), které zlepšují schopnost Claude vytvářet dokumenty, prezentace a další typy souborů. Tyto dovednosti jsou modulární balíčky instrukcí uložené ve formátu SKILL.md, které Claude automaticky aktivuje, když jsou relevantní pro daný úkol. Předinstalované dovednosti se zaměřují především na vytváření dokumentů v různých formátech.

Pro uživatele, kteří mají nainstalované rozšíření [Claude in Chrome](https://claude.com/chrome), přibývá možnost zadávat úkoly vyžadující práci v prohlížeči. Agent tak může například vyhledat informace na webu a následně je zpracovat do požadovaného formátu ve složce.

Významnou vlastností je možnost řazení úkolů do fronty. Uživatel nemusí čekat na dokončení jednoho úkolu, než zadá další. Claude zpracovává požadavky paralelně, což podle Anthropic připomíná spíše zanechávání zpráv kolegovi než klasickou konverzaci tam a zpět.

## První uživatelské zkušenosti


**Vytvoření kompetitivní analýzy** dopadlo lépe. Cowork položil relevantní upřesňující otázky, vytvořil plán zahrnující webový průzkum a použití dovednosti pro DOCX, a během přibližně pěti minut vygeneroval použitelný dokument. Problematické bylo, že mezi artefakty se kromě očekávaného dokumentu Word objevil i soubor create-brief.js obsahující kód použitý k vytvoření dokumentu. Pro netechnického uživatele jde o matoucí informaci, která by měla být ve výchozím stavu skrytá.

**Vytvoření prezentace z dokumentu** ilustrovalo další úskalí rozhraní. Proces zahrnoval čtení zdrojového dokumentu, vytvoření jednotlivých HTML stránek pro každý snímek a následnou kompilaci do PPTX. Uživatel viděl průběžně vznikající HTML soubory, což vyvolávalo zmatek, dokud nepochopil, že jde o mezikrok. Finální prezentace byla použitelná, ale cesta k ní byla zbytečně stresující.


## Současné problémy

Seznam problémů v současné verzi je rozsáhlý. Konektory se nepřipojují spolehlivě. Příkazy terminálu selhávají s děsivě vypadajícími chybovými hláškami. Lokální soubory jako DOCX se nenačítají při kliknutí na tlačítko zobrazení, ačkoli fungují v kontextových zprávách nástroje. Rozhraní zobrazuje příliš mnoho kontextu, příliš mnoho skriptů a obecně odhaluje příliš mnoho z vnitřního fungování. Systém se také dotazuje na povolení k otevření souborů nepřiměřeně často a připojuje MCP servery, o které uživatel nežádal. Na tom všem je vidět dědictví Claude Code, které přesně tohle dělá, ale podstatně zkušenějším uživatelům. 

Paradoxní je také vydání pro macOS s primárním zaměřením na vytváření souborů Microsoft Office (DOCX, PPTX), které systém následně nabízí otevřít v aplikaci Pages. Uživatelé by v mnoha případech asi preferovali jednodušší formát jako Markdown.

## Otázka cílového publika

Základní otázka, kterou si kladou první uživatelé, zní: pro koho přesně je Cowork určen? Průnik mezi uživateli Claude Code a potenciálními uživateli Cowork je v současnosti téměř úplný. Je obtížné si představit uživatele s předplatným Claude Max na macOS, který rozumí práci s agenty, a zároveň by preferoval omezenější desktopovou aplikaci před terminálem.

Problém spočívá v tom, že Cowork je příliš tenká vrstva nad Claude Code. Pro netechnické uživatele zobrazuje příliš mnoho implementačních detailů: pracovní soubory, mezikroky v HTML, skripty. Pro technicky zdatné uživatele je naopak příliš omezený oproti plnému Claude Code. Produkt tak sedí v nezřetelném středu a tým bude muset zvolit optimalizaci pro jednu nebo druhou skupinu, aby získal nové publikum. Osobně mi ale znakové rozhraní sedí a považuji to pro mnoho aplikací za dobré řešení, překvapivě právě moje správa projektů je takto založena. 

## Bezpečnostní omezení a rizika

Anthropic v oznámení věnuje značný prostor bezpečnostním aspektům. Uživatel má plnou kontrolu nad tím, ke kterým složkám a konektorům Claude přistupuje. Model si před provedením významných akcí vyžádá souhlas, což umožňuje průběžnou korekci směru práce, byť frekvence těchto dotazů je podle prvních ohlasů nadměrná.

Existují však rizika, která nelze zcela eliminovat. Claude může při chybné interpretaci instrukcí provést destruktivní akce, například smazat soubory. Anthropic doporučuje formulovat pokyny co nejpřesněji, zejména u operací, které mohou způsobit nevratné změny.

Druhým významným rizikem jsou takzvané prompt injection útoky. Jedná se o techniku, kdy útočník vloží do obsahu, se kterým Claude pracuje, instrukce, které změní chování agenta. Anthropic implementoval obranné mechanismy, ale přiznává, že zabezpečení agentních systémů zůstává aktivní oblastí vývoje v celém odvětví. Podrobnější informace o bezpečném používání firma zveřejnila v [nápovědě](https://support.claude.com/en/articles/13364135-using-cowork-safely).

## Dostupnost a cena

| Parametr | Hodnota |
|----------|---------|
| Platforma | macOS (desktopová aplikace Claude) |
| Požadovaný tarif | Claude Max |
| Cena tarifu Max | 100 USD/měsíc (5× limity Pro) nebo 200 USD/měsíc (20× limity Pro) |
| Fáze | Výzkumný náhled |
| Alternativa pro ostatní | [Čekací seznam](https://forms.gle/mtoJrd8kfYny29jQ9) |

Claude Max je prémiový tarif Anthropic určený pro intenzivní uživatele. Za 100 dolarů měsíčně poskytuje pětinásobek využití oproti tarifu Pro, varianta za 200 dolarů pak dvacetinásobek. Tarif zahrnuje přístup k nejnovějším modelům včetně Claude Opus 4.5 a přednostní přístup k novým funkcím.

Pro uživatele Windows zatím Cowork není dostupný. Anthropic plánuje rozšíření platformové podpory i přidání synchronizace mezi zařízeními, konkrétní termíny však nezveřejnil.

## Kontext a hodnocení

Vznik Cowork není náhodný. Claude Code se během posledního roku stal jedním z nejúspěšnějších produktů Anthropic a uživatelé ho začali využívat daleko za hranicemi programování. Nástroj původně určený vývojářům našel uplatnění při výzkumu, zpracování dokumentů nebo automatizaci administrativních úkolů. Cowork je reakcí na tento organický vývoj a pokusem zpřístupnit agentní schopnosti širšímu publiku.

Označení výzkumný náhled je v tomto případě přesné. Cowork ukazuje směr, kterým se Anthropic chce vydat, ale současná implementace trpí řadou problémů od nefunkčních konektorů po nepromyšlené uživatelské rozhraní. Pozitivní je, že samotný agentní mechanismus generuje kvalitnější výstupy než běžný chat. Otázkou zůstává, zda se Anthropic podaří najít správnou rovnováhu mezi transparentností procesu a jednoduchostí pro netechnické uživatele, nebo zda Cowork zůstane produktem bez jasně definovaného publika.