---
slug: "cccf"
url: "/mobilnisite/slovnik/cccf/"
type: "slovnik"
title: "CCCF – Call Continuity Control Function"
date: 2025-01-01
abbr: "CCCF"
fullName: "Call Continuity Control Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cccf/"
summary: "Call Continuity Control Function (CCCF) je síťový prvek zavedený ve specifikaci 3GPP Release 7 pro správu předávání hlasových hovorů mezi okruhově komutovanou (CS) doménou a doménou IP Multimedia Subs"
---

CCCF je síťová funkce, která spravuje předávání hlasových hovorů mezi okruhově komutovanou doménou a doménou IMS, aby zajistila plynulé pokračování hovoru, například při přepínání mezi mobilní sítí a Wi-Fi.

## Popis

Call Continuity Control Function (CCCF) je klíčová komponenta v architektuře IP Multimedia Subsystem (IMS), specificky definovaná pro podporu funkce Voice Call Continuity ([VCC](/mobilnisite/slovnik/vcc/)). Funguje jako aplikační server ([AS](/mobilnisite/slovnik/as/)), který kotví hlasové hovory, aby umožnil přenos domény mezi okruhově komutovanou ([CS](/mobilnisite/slovnik/cs/)) doménou (např. tradiční hlas GSM/UMTS) a doménou IMS/[PS](/mobilnisite/slovnik/ps/) (paketově komutovanou, např. VoIP přes LTE nebo Wi-Fi). Když uživatel s podporou VCC zahájí nebo přijme hovor, je vyvolána CCCF, která řídí směrování hovoru a spravuje potřebnou signalizaci pro případná předání. Rozhraní k Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) zprostředkovává přes rozhraní [ISC](/mobilnisite/slovnik/isc/) (IMS Service Control) a může komunikovat s CS doménou přes [MGCF](/mobilnisite/slovnik/mgcf/) (Media Gateway Control Function) nebo přímo s [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Centre) pomocí protokolu CAMEL (Customised Applications for Mobile network Enhanced Logic) či jiných signalizačních protokolů v závislosti na nasazení sítě.

Z architektonického hlediska obsahuje CCCF logiku pro provedení výběru domény při zahájení a ukončení hovoru, přičemž rozhoduje, zda má být hovor navázán v CS nebo IMS doméně na základě registrace uživatele, jeho schopností a stavu sítě. Během aktivního hovoru monitoruje spouštěcí události – například změny v technologii radiového přístupu (jako přechod z Wi-Fi do pokrytí mobilní sítí) – které vyžadují přenos domény. Po přijetí žádosti o přenos CCCF koordinuje spolupráci s dalšími síťovými funkcemi za účelem přesměrování větve hovoru, aktualizace mediální cesty a zajištění kontinuity signalizace. To zahrnuje procedury jako provedení řízení hovoru třetí stranou, kde CCCF funguje jako back-to-back uživatelský agent (B2BUA) pro propojení obou domén, přičemž udržuje relaci hovoru při výměně podkladového transportu.

Mezi klíčové vnitřní komponenty CCCF patří funkce přenosu domény, která zajišťuje logiku a signalizaci pro přepínání domén; stavový automat hovoru, který sleduje stav aktivního hovoru napříč doménami; a rozhraní k údajům o účastníkovi (např. pro informace o předplatném VCC). Její role přesahuje základní předání: spravuje také funkce jako aspekty duálního rádia (kdy zařízení může současně používat samostatná rádia pro CS a PS) a zajišťuje, že doplňkové služby (např. čekání, přesměrování hovoru) jsou během přenosů zachovány. CCCF spolupracuje s dalšími entitami VCC, jako je funkce Network Domain Selection (NeDS) pro počáteční výběr domény a prostředí služby CAMEL pro interakce s CS doménou, čímž vytváří komplexní řešení pro kontinuitu hovorů v raných nasazeních IMS.

## K čemu slouží

CCCF byla vytvořena, aby řešila problém udržení kontinuity hlasového hovoru při vývoji mobilních sítí směrem k plně IP architekturám se zavedením IMS ve specifikaci 3GPP Release 5. Před VCC a CCCF byly hlasové hovory převážně okruhově komutované a nově se objevující VoIP služby přes IMS nebo Wi-Fi fungovaly v izolovaných doménách, což vedlo k přerušeným hovorům, když uživatelé přecházeli mezi těmito doménami. Například uživatel na Wi-Fi VoIP hovoru by při ztrátě pokrytí Wi-Fi ztratil spojení, pokud by síť nemohla předat hovor do mobilní CS sítě. CCCF to řeší tím, že poskytuje centralizovaný řídicí bod pro správu plynulých přechodů, což operátorům umožňuje nabízet konvergované hlasové služby a podporuje adopci hlasu založeného na IMS bez obětování spolehlivosti.

Historicky vycházela motivace z potřeby podpory Fixed-Mobile Convergence (FMC) a raných předchůdců Voice over LTE (VoLTE), kde bylo zajištění kontinuity služby klíčové pro přijetí uživateli. Bez CCCF by zařízení s duálním režimem (podporující jak CS, tak PS hlas) čelila přerušením služby, což by omezovalo praktičnost nasazení IMS. CCCF jako součást frameworku VCC umožnila operátorům využít stávající CS infrastrukturu při migraci na IMS, čímž poskytla plynulou přechodovou cestu. Řešila omezení dřívějších přístupů, jako proprietární řešení nebo jednoduché síťové přepínání, standardizací procedur předání v rámci 3GPP, čímž zajistila interoperabilitu a konzistentní uživatelský zážitek napříč více-dodavatelskými sítěmi.

## Klíčové vlastnosti

- Kotví hlasové hovory pro přenos domény mezi CS a IMS doménami
- Funguje jako IMS aplikační server (AS) pro servisní logiku služby Voice Call Continuity (VCC)
- Provádí výběr domény při zahájení a ukončení hovoru na základě stavu účastníka a sítě
- Koordinuje řízení hovoru třetí stranou za účelem přesměrování média a signalizace během předání
- Poskytuje rozhraní k S-CSCF přes ISC a k CS síti přes protokoly CAMEL nebo MGCF
- Udržuje stav hovoru a doplňkové služby během přechodů mezi doménami

## Definující specifikace

- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details

---

📖 **Anglický originál a plná specifikace:** [CCCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/cccf/)
