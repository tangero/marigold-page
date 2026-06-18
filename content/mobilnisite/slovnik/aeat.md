---
slug: "aeat"
url: "/mobilnisite/slovnik/aeat/"
type: "slovnik"
title: "AEAT – Advanced Emergency Alert Table"
date: 2025-01-01
abbr: "AEAT"
fullName: "Advanced Emergency Alert Table"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aeat/"
summary: "AEAT je strukturovaná datová tabulka definovaná v 3GPP pro vysílání rozšířených nouzových upozornění do mobilních zařízení. Umožňuje multimediální upozornění s přesným geografickým cílením a podporuje"
---

AEAT je standardizovaná datová tabulka definovaná 3GPP pro vysílání rozšířených nouzových upozornění s multimediálním obsahem a přesným geografickým cílením do mobilních zařízení, která podporuje systémy varování obyvatelstva.

## Popis

Advanced Emergency Alert Table (AEAT) je standardizovaná datová struktura specifikovaná v 3GPP TS 26.917, která definuje formát a obsah pro vysílání rozšířených nouzových upozornění do uživatelského zařízení (UE) prostřednictvím buněčných vysílacích kanálů. Slouží jako kontejner pro multimediální zprávy varování obyvatelstva, které přesahují pouhý text a zahrnují obrázky, zvuk, video a přesné geografické cílení. AEAT je navržen tak, aby byl přenášen přes stávající vysílací mechanismy, jako je Cell Broadcast ([CB](/mobilnisite/slovnik/cb/)) v LTE a NR, nebo přes System Information Blocks (SIBy), což zajišťuje distribuci v široké oblasti bez zahlcení jednoadresových kanálů.

Z architektonického hlediska je AEAT generován Cell Broadcast Entity ([CBE](/mobilnisite/slovnik/cbe/)) nebo aplikačním serverem systému varování obyvatelstva ([PWS](/mobilnisite/slovnik/pws/)), který skládá výstražnou zprávu podle schématu AEAT. To zahrnuje povinné prvky, jako je jedinečný identifikátor upozornění, úroveň závažnosti, kategorie (např. zemětřesení, tsunami, únos dítěte) a doba platnosti. Volitelné multimediální komponenty – jako jsou obrázky [JPEG](/mobilnisite/slovnik/jpeg/), zvuk [AMR-WB](/mobilnisite/slovnik/amr-wb/)+ nebo videoklipy [HEVC](/mobilnisite/slovnik/hevc/) – jsou v tabulce odkazovány pomocí [URI](/mobilnisite/slovnik/uri/) nebo vloženy jako binární data. AEAT také obsahuje geoprostorové cílení pomocí tvarů, jako jsou polygony nebo kruhy, což umožňuje, aby upozornění byla relevantní pouze pro UE v konkrétních geografických oblastech, a snižuje tak zbytečný poplach uživatelů.

Klíčové komponenty AEAT zahrnují hlavičku upozornění (Alert Header), která obsahuje metadata jako verzi protokolu a identifikátor zprávy; informační blok upozornění (Alert Info Block), který obsahuje text srozumitelný člověku ve více jazycích; a blok multimediálních objektů (Multimedia Objects block), který odkazuje nebo obsahuje binární data pro obrázky, zvuk nebo video. Dále blok geografického cílení (Geographic Targeting block) využívá formáty Well-Known Text (WKT) nebo GeoJSON k definování postižené oblasti. AEAT je kódován pomocí kompaktního binárního formátu (často založeného na ASN.1 [PER](/mobilnisite/slovnik/per/) nebo podobném efektivním kódování), aby se minimalizovala režie vysílání a zajistil rychlý přenos.

V síti je AEAT doručován prostřednictvím Cell Broadcast Center (CBC) k základnovým stanicím (eNodeB/gNB), které jej vysílají přes rozhraní vzduchu pomocí System Information Block Type 12 (SIB12) v LTE nebo SIB9 v NR, nebo prostřednictvím vyhrazených zpráv Cell Broadcast. Po přijetí klient PWS v UE analyzuje AEAT, zkontroluje geografickou relevanci na základě polohy zařízení (pokud je dostupná) a zobrazí upozornění uživateli s multimediálními komponentami, pokud je podporováno. Role AEAT je klíčová v moderních systémech varování obyvatelstva, neboť umožňuje orgánům doručovat podrobné, akční informace během mimořádných událostí, čímž zvyšuje veřejnou bezpečnost a účinnost zásahu.

## K čemu slouží

AEAT byl vytvořen, aby řešil omezení dřívějších systémů varování obyvatelstva, jako je Earthquake and Tsunami Warning System (ETWS) a Commercial Mobile Alert System (CMAS), které byly primárně textové a postrádaly multimediální schopnosti. Před zavedením AEAT byla nouzová upozornění omezena na krátké textové zprávy (až 90 znaků v některých implementacích) s omezenou přesností geografického cílení. To bránilo doručování bohatých, kontextových informací – jako jsou mapy, evakuační trasy nebo instruktážní videa – které jsou klíčové během složitých mimořádných událostí, jako jsou přírodní katastrofy nebo teroristické útoky. AEAT standardizuje formát, který tyto pokročilé funkce umožňuje, a zajišťuje interoperabilitu mezi různými síťovými operátory, výrobci zařízení a národními varovnými systémy.

Historicky potřeba AEAT vyplynula ze skutečných událostí, kde se pouze textová upozornění ukázala jako nedostatečná. Například při zemětřesení je mapa zobrazující epicentrum a postižené zóny informativnější než textový popis. Podobně pro upozornění na únos dítěte může fotografie pohřešovaného dítěte významně napomoci rozpoznání veřejností. 3GPP tyto mezery identifikovalo a zahájilo práci ve verzi 15 (Release 15) na definici tabulkové struktury, která by mohla nést multimediální obsah při zachování zpětné kompatibility s existujícími PWS frameworky. To bylo motivováno globálními regulačními trendy, jako je evropský European Electronic Communications Code (EECC) a americké požadavky WEA 2.0, které nařizovaly rozšířené schopnosti varování obyvatelstva.

AEAT řeší problém fragmentovaných, proprietárních formátů upozornění tím, že poskytuje jednotný standard 3GPP. Umožňuje orgánům vysílat konzistentní upozornění s bohatým obsahem napříč sítěmi LTE a 5G bez ohledu na výrobce UE nebo mobilního operátora. To zajišťuje, že všichni uživatelé v postižené oblasti obdrží stejné kvalitní informace, což zlepšuje výsledky v oblasti veřejné bezpečnosti. Kromě toho efektivní kódování AEAT a podpora přírůstkových aktualizací snižují zatížení sítě a spotřebu baterie v zařízeních, čímž řeší praktické problémy nasazení.

## Klíčové vlastnosti

- Podporuje vkládání multimediálního obsahu (obrázky, zvuk, video) pro bohatší upozornění
- Umožňuje přesné geografické cílení pomocí polygonů, kruhů nebo jiných geofencí
- Definuje standardizované binární kódování (např. založené na ASN.1) pro efektivní vysílání
- Zahrnuje podporu vícejazyčného textu pro mezinárodní kompatibilitu
- Poskytuje rozšiřitelné kategorie upozornění a úrovně závažnosti pro různé typy mimořádných událostí
- Zachovává zpětnou kompatibilitu se staršími systémy ETWS a CMAS

## Související pojmy

- [CMAS – Commercial Mobile Alert Service](/mobilnisite/slovnik/cmas/)

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [AEAT na 3GPP Explorer](https://3gpp-explorer.com/glossary/aeat/)
