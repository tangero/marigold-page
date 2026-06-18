---
slug: "lro"
url: "/mobilnisite/slovnik/lro/"
type: "slovnik"
title: "LRO – Last Routing Option"
date: 2025-01-01
abbr: "LRO"
fullName: "Last Routing Option"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lro/"
summary: "Mechanismus směrování hovorů v IP Multimedia Subsystem (IMS), který definuje poslední pokus o směrování relace, když byly vyčerpány všechny ostatní směrovací logiky. Slouží jako záchranná síť pro zpra"
---

LRO je poslední pokus o směrování v IMS pro relaci, když všechny ostatní směrovací logiky selžou; funguje jako záchranná síť pro přesměrování hovoru na výchozí cíl, například na hlasový server.

## Popis

Last Routing Option (LRO) je funkční komponenta ve služební vrstvě IMS, konkrétně součást logiky Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) a jejího přidruženého Application Server ([AS](/mobilnisite/slovnik/as/)). Nejde o samostatný síťový prvek, ale o konfigurovatelnou sadu pravidel nebo určený aplikační spouštěč, který se vykoná jako poslední krok v komplexním řetězci vyvolání služeb. Když terminál IMS zahájí relaci (např. hlasový nebo videohovor), S-CSCF zpracovává počáteční požadavek [SIP](/mobilnisite/slovnik/sip/) INVITE prostřednictvím série filtračních kritérií (iFCs) definovaných v profilu účastníka. Tato iFCs postupně vyvolávají různé Application Servery, které poskytují služby jako přesměrování hovoru, transformace čísla nebo hlasová schránka.

LRO se uplatní poté, co jsou všechna počáteční filtrační kritéria zpracována a nebylo dosaženo definitivního ukončení relace ani úspěšného směrování. K tomu typicky dochází ve scénářích, jako je neregistrovaný uživatel, neplatná cílová adresa nebo když všechny vyvolané služby odmítnou relaci dále zpracovat. V tomto okamžiku aktivuje servisní logika S-CSCF předkonfigurovanou Last Routing Option. LRO je v podstatě posledním, nepodmíněným iFC nebo vestavěným chováním S-CSCF, které odkazuje na konkrétní Application Server určený pro zpracování těchto případů 'poslední instance'.

Tento finální Application Server, často Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) nebo specializovaný hlasový server, poté převezme kontrolu nad relací. Jeho primární funkcí je poskytnout řízené ukončení pokusu o hovor. To obvykle zahrnuje přehrání vhodného hlášení volající straně (např. "Vámi volané číslo není v provozu" nebo "Účastník není dostupný") a následné uvolnění prostředků relace. Případně lze LRO nakonfigurovat tak, aby hovor směroval na výchozí cíl, jako je operátor nebo zákaznické centrum. Tím, že poskytuje tento deterministický finální krok, LRO zabraňuje ponechání relací v nejednoznačném stavu v síti, zajišťuje konzistentní uživatelský zážitek u neúspěšných hovorů a napomáhá úklidu síťových prostředků.

## K čemu slouží

Last Routing Option byl zaveden, aby odstranil kritickou mezeru v raném modelu provádění služeb IMS. IMS bylo navrženo s vysokou mírou flexibility, umožňující víceřetězcové Application Servery manipulovat s relací prostřednictvím počátečních filtračních kritérií. Tento řetězcový model provádění však postrádal garantovaný, definitivní koncový bod. Pokud řetězec servisní logiky skončil bez konečného rozhodnutí (např. žádný [AS](/mobilnisite/slovnik/as/) nepřijal hovor k finálnímu zpracování), zůstal by [S-CSCF](/mobilnisite/slovnik/s-cscf/) s požadavkem na relaci, který nemohl dále zpracovat, což by mohlo vést k odeslání chyby protokolu [SIP](/mobilnisite/slovnik/sip/) (jako 480 Temporarily Unavailable nebo 404 Not Found) bez uživatelsky přívětivého kontextu.

Tato situace byla problematická jak pro síťové operátory, tak pro koncové uživatele. Pro operátory vedla k nekonzistentnímu zpracování chyb, ztěžovala odstraňování problémů a plýtvala síťovými prostředky na relace, které nakonec selhaly bez patřičného zaznamenání nebo hlášení. Pro koncové uživatele to mělo za následek generické nebo matoucí tóny/oznámení o selhání namísto informativních hlášení. LRO byl vytvořen, aby toto vyřešil zavedením deterministické, konfigurovatelné finální akce pro každou relaci, která prochází servisní vrstvou S-CSCF. Zajišťuje, že žádný požadavek na relaci 'nepropadne' skrze servisní logiku.

Navíc LRO poskytuje klíčový mechanismus pro kontinuitu služeb a řádné snížení výkonu. Umožňuje operátorům definovat záložní chování, jako je směrování na základní hlasovou službu nebo záložní AS, v případě, že primární aplikační servery jsou nedostupné nebo nefungují. Tím se zlepšuje odolnost sítě a zákaznický zážitek. Jeho specifikace v 3GPP TS 23.167, která pokrývá nouzové relace IMS, také zdůrazňuje jeho roli v zajištění definitivního finálního ošetření pokusů o nouzové hovory, i když normální směrovací logika selže, čímž podporuje splnění regulatorních požadavků pro nouzové služby.

## Klíčové vlastnosti

- Provede se jako poslední krok v servisní logice S-CSCF po zpracování všech počátečních filtračních kritérií
- Poskytuje deterministický, konfigurovatelný koncový bod pro nevyřešené požadavky na relaci
- Typicky spouští finální Application Server, často MRF pro hlášení
- Zabraňuje nejednoznačným stavům relace a zajišťuje úklid prostředků
- Umožňuje konzistentní uživatelský zážitek pro scénáře neúspěšných hovorů
- Podporuje robustnost služeb tím, že funguje jako záložní mechanismus

## Definující specifikace

- **TS 23.167** (Rel-19) — IMS Emergency Sessions

---

📖 **Anglický originál a plná specifikace:** [LRO na 3GPP Explorer](https://3gpp-explorer.com/glossary/lro/)
