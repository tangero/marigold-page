---
slug: "cwe"
url: "/mobilnisite/slovnik/cwe/"
type: "slovnik"
title: "CWE – Common Weakness Enumeration"
date: 2025-01-01
abbr: "CWE"
fullName: "Common Weakness Enumeration"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/cwe/"
summary: "CWE je standardizovaný seznam bezpečnostních slabin softwaru a hardwaru spravovaný MITRE a odkazovaný 3GPP. Poskytuje společný jazyk pro identifikaci, popis a kategorizaci bezpečnostních zranitelností"
---

CWE je standardizovaný seznam bezpečnostních slabin softwaru a hardwaru, který spravuje MITRE a odkazuje na něj 3GPP. Poskytuje společný jazyk pro identifikaci a kategorizaci zranitelností v telekomunikačních systémech.

## Popis

Common Weakness Enumeration (CWE) je komunitou vyvíjený formální seznam běžných bezpečnostních slabin softwaru a hardwaru. V kontextu norem 3GPP slouží CWE jako základní taxonomie pro bezpečnostní analýzu, hodnocení zranitelností a modelování hrozeb síťových funkcí, protokolů a rozhraní. Poskytuje standardizovanou slovní zásobu, která umožňuje bezpečnostním výzkumníkům, výrobcům síťových zařízení a mobilním operátorům konzistentně identifikovat a komunikovat o bezpečnostních nedostatcích, které by mohly ovlivnit 5G sítě, od rádiové přístupové sítě (RAN) po síť jádra a systémy správy.

Rámec CWE funguje prostřednictvím hierarchického klasifikačního systému, který organizuje slabiny do kategorií, pohledů a jednotlivých záznamů. Každý záznam CWE obsahuje jedinečný identifikátor, popisný název, podrobný technický popis slabiny, potenciální důsledky při zneužití, běžné vzorce útoků a navrhované strategie zmírnění. Taxonomie pokrývá široké spektrum zranitelností včetně přetečení bufferu, injekčních chyb, nevhodného ověřování, nezabezpečených výchozích nastavení a kryptografických problémů. Tento strukturovaný přístup umožňuje systematické bezpečnostní testování a procesy kontroly kódu v průběhu celého životního cyklu vývoje systémů kompatibilních s 3GPP.

V rámci bezpečnostní architektury 3GPP je CWE integrováno do specifikací bezpečnostního zajištění, zejména v 3GPP TS 33.916, která definuje metodologii bezpečnostního zajištění pro 5G systémy. Rámec podporuje principy zabezpečení již při návrhu tím, že poskytuje konkrétní příklady zranitelností, kterým je třeba předcházet během návrhu a implementace systému. Záznamy CWE jsou mapovány na konkrétní síťové funkce a rozhraní 3GPP, což umožňuje bezpečnostním týmům provádět cílená hodnocení zranitelností na základě hodnocených architektonických komponent. Toto mapování zajišťuje, že bezpečnostní testování pokrývá relevantní útočné plochy specifické pro telekomunikační sítě.

Praktická aplikace CWE v ekosystémech 3GPP zahrnuje více zúčastněných stran. Výrobci síťových zařízení používají CWE během vývoje k identifikaci a odstranění běžných chyb v kódu a nedostatků v návrhu. Mobilní operátoři odkazují na CWE během bezpečnostních auditů a testování průniku nasazených sítí. Normalizační orgány používají CWE k definování bezpečnostních požadavků a testovacích metodologií. Neustálý vývoj rámce, poháněný komunitními příspěvky a objevy zranitelností z reálného světa, zajišťuje, že zůstává relevantní vůči novým hrozbám pro 5G sítě, včetně těch zaměřených na síťové segmenty, edge computing a nasazení IoT.

## K čemu slouží

CWE bylo vytvořeno, aby řešilo zásadní výzvu nekonzistentní identifikace a komunikace zranitelností napříč komunitou kybernetické bezpečnosti. Před standardizovanými taxonomiemi, jako je CWE, používali bezpečnostní výzkumníci, výrobci a operátoři pro popis stejných zranitelností různou terminologii, což vedlo ke zmatkům, neefektivní nápravě a mezerám v bezpečnostním pokrytí. Tato nekonzistence byla obzvláště problematická v komplexních ekosystémech s více dodavateli, jako jsou sítě 3GPP, kde různé komponenty od různých výrobců musí bezpečně spolupracovat.

Hlavní motivací pro přijetí CWE v rámci norem 3GPP bylo vytvoření společného jazyka pro bezpečnostní zranitelnosti, kterému by všichni zúčastnění rozuměli a který by konzistentně používali. To umožňuje efektivnější spolupráci mezi výrobci síťových zařízení, mobilními operátory, bezpečnostními výzkumníky a normalizačními orgány. Tím, že poskytuje standardizovaný způsob popisu slabin, CWE usnadňuje systematické bezpečnostní testování, jasnější hlášení zranitelností a efektivnější správu záplat napříč celým 5G dodavatelským řetězcem.

CWE řeší specifická omezení předchozích přístupů ke klasifikaci zranitelností v telekomunikacích. Dřívější metody se často spoléhaly na ad-hoc popisy nebo proprietární klasifikační systémy, které nebyly interoperabilní mezi různými organizacemi. CWE poskytuje komplexní, veřejně dostupnou taxonomii, která pokrývá jak známé, tak nově se objevující typy zranitelností. Její integrace do specifikací 3GPP pomáhá zajistit, aby byly bezpečnostní aspekty začleněny do návrhu sítě od samého počátku, a nikoli řešeny dodatečně, čímž se posiluje celkové bezpečnostní postavení 5G sítí vůči vyvíjejícím se hrozbám.

## Klíčové vlastnosti

- Standardizovaná taxonomie zranitelností s hierarchickou klasifikací
- Komplexní pokrytí bezpečnostních slabin softwaru a hardwaru
- Podrobné technické popisy včetně vzorců útoků a důsledků
- Mapování na síťové funkce a rozhraní 3GPP pro cílené hodnocení
- Komunitou řízená správa a průběžné aktualizace
- Integrace s metodologiemi bezpečnostního zajištění ve specifikacích 3GPP

## Definující specifikace

- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)

---

📖 **Anglický originál a plná specifikace:** [CWE na 3GPP Explorer](https://3gpp-explorer.com/glossary/cwe/)
