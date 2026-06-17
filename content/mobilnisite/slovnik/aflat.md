---
slug: "aflat"
url: "/mobilnisite/slovnik/aflat/"
type: "slovnik"
title: "AFLAT – Autocorrelation Fixed Point LAttice Technique"
date: 2025-01-01
abbr: "AFLAT"
fullName: "Autocorrelation Fixed Point LAttice Technique"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/aflat/"
summary: "AFLAT je technika vektorové kvantizace používaná v řečovém kodeku GSM Half Rate (HR). Konkrétně kvantizuje koeficienty lineárně prediktivního kódování (LPC), které reprezentují spektrální obálku řeči."
---

AFLAT je technika vektorové kvantizace používaná v řečovém kodeku GSM Half Rate pro efektivní kvantizaci koeficientů lineárně prediktivního kódování (LPC) pro řečové kódování s nízkou přenosovou rychlostí.

## Popis

AFLAT (Autocorrelation Fixed Point LAttice Technique) je klíčový algoritmus v řečovém kodeku GSM Half Rate ([HR](/mobilnisite/slovnik/hr/)) definovaném v 3GPP specifikacích řady TS 46. Funguje na principu lineárně prediktivního kódování ([LPC](/mobilnisite/slovnik/lpc/)), metody, která modeluje lidský hlasový trakt jako digitální filtr. LPC analýza produkuje sadu koeficientů popisujících spektrální tvar neboli formanty krátkého segmentu řeči. Tyto koeficienty jsou klíčové pro kvalitní syntézu řeči, ale pro přenos přes rádiové kanály s omezenou šířkou pásma vyžadují efektivní reprezentaci. AFLAT tento problém řeší poskytnutím sofistikované metody vektorové kvantizace šité na míru těmto LPC parametrům.

Technika funguje tak, že nejprve transformuje LPC koeficienty do robustnější a lépe kvantovatelné reprezentace, často zahrnující reflexní koeficienty nebo lineární spektrální frekvence ([LSF](/mobilnisite/slovnik/lsf/)). AFLAT následně aplikuje proces vektorové kvantizace, při kterém se prohledává kodebook – předdefinovaná sada typických spektrálních vektorů – aby se našla nejbližší shoda se vstupním LPC vektorem. Místo celé sady koeficientů se přenáší index tohoto odpovídajícího kódového slova, což drasticky snižuje přenosovou rychlost. Část názvu 'Fixed Point LAttice' odkazuje na matematickou strukturu použitou v návrhu kodebooku a vyhledávacího algoritmu, která je optimalizována pro stabilitu a výpočetní efektivitu v pevnou řádovou čárkou digitálních signálových procesorech, což bylo běžné hardwarové omezení v raných mobilních telefonech.

V architektuře kodeku GSM HR je AFLAT klíčovou součástí řečového kodéru. Poté, co LPC analýza extrahuje parametry spektrální obálky, AFLAT tyto parametry kvantizuje. Kvantizovaná LPC informace je pak zabalena do řečového rámce spolu s dalšími kvantizovanými parametry, jako je základní tón a excitační signály. V dekodéru se přijatý index použije k načtení kvantizovaného LPC vektoru z identického kodebooku a tento vektor se použije ke konfiguraci syntetizačního filtru pro rekonstrukci řečového signálu. Přesnost a efektivita kvantizace AFLAT přímo ovlivňuje kompromis mezi kvalitou řeči a úsporou přenosové rychlosti, která definuje Half Rate kanál pracující přibližně na 5,6 kbit/s ve srovnání s 13 kbit/s u Full Rate.

Role AFLAT je základní pro fungování kodeku GSM HR. Tím, že umožňuje přesnou a kompaktní reprezentaci perceptuálně nejvýznamnější části řečového signálu – spektrální obálky – umožňuje systému alokovat ušetřené bity do dalších aspektů kódovacího řetězce nebo jednoduše snížit celkovou požadovanou šířku pásma kanálu. Tato efektivita byla v 90. letech pro síťové operátory prvořadá, protože efektivně zdvojnásobila kapacitu hovorů v daném přidělení rádiového spektra. Návrh techniky pro aritmetiku s pevnou řádovou čárkou zajišťoval, že ji bylo možné implementovat v energeticky úsporných a cenově výhodných [DSP](/mobilnisite/slovnik/dsp/) své doby, což učinilo GSM Half Rate komerčně životaschopnou technologií.

## K čemu slouží

AFLAT byl vytvořen, aby vyřešil kritický problém spektrální efektivity v raných digitálních celulárních sítích. Řečový kodek GSM Full Rate ([FR](/mobilnisite/slovnik/fr/)), představený koncem 80. let, poskytoval dobrou kvalitu, ale spotřebovával významných 13 kbit/s šířky pásma rádiového kanálu. S růstem počtu účastníků čelili síťoví operátoři kapacitním omezením. Kodek GSM Half Rate ([HR](/mobilnisite/slovnik/hr/)) byl standardizován, aby zdvojnásobil kapacitu snížením přenosové rychlosti řeči přibližně na 5,6 kbit/s. Použití agresivnější verze FR kvantizačních technik by však vedlo k nepřijatelnému zhoršení kvality řeči. AFLAT byl vyvinut jako specializovaná, pokročilá kvantizační technika, která umožnila toto drastické snížení přenosové rychlosti při zachování srozumitelnosti a přijatelné hlasové kvality.

Historický kontext představovala intenzivní konkurence a rychlý růst GSM v 90. letech. Síťová infrastruktura a licence na spektrum byly významné kapitálové výdaje. Jakákoli technologie, která mohla zvýšit počet současných hovorů na stávající infrastruktuře bez zhoršení uživatelského zážitku, poskytovala přímou konkurenční a finanční výhodu. Předchozí přístupy ke kvantizaci [LPC](/mobilnisite/slovnik/lpc/) v dřívějších kodecích byly méně efektivní a náchylnější ke kvantizačnímu šumu, který se projevuje jako tlumená nebo robotická řeč. Účelem AFLAT bylo poskytnout matematicky robustní metodu komprese LPC informace s minimální percepční ztrátou, což umožnilo, aby se kodek Half Rate stal praktickým nástrojem pro správu síťového provozu během špičky nebo v hustě obydlených městských oblastech.

Technika navíc řešila omezení hardwarové implementace. Mobilní telefony vyžadovaly algoritmy schopné běžet v reálném čase na nízkopříkonových digitálních signálových procesorech s pevnou řádovou čárkou. Návrh 'Fixed Point LAttice' v AFLAT zajišťoval výpočetní stabilitu a efektivitu v rámci těchto omezení, čímž se funkce Half Rate stala realizovatelnou pro telefony masového trhu. Bez takto efektivního kvantizačního jádra by byl kodek Half Rate buď příliš výpočetně složitý, nebo příliš nekvalitní pro komerční nasazení.

## Klíčové vlastnosti

- Specializovaná vektorová kvantizace pro koeficienty lineárně prediktivního kódování (LPC)
- Navržena pro implementaci na digitálním signálovém procesoru (DSP) s pevnou řádovou čárkou
- Využívá strukturovaný kodebook založený na principu mřížky pro efektivní vyhledávání
- Umožňuje přenosovou rychlost ~5,6 kbit/s řečového kanálu GSM Half Rate (HR)
- Optimalizována pro minimalizaci percepčního zkreslení v kvantizované spektrální obálce
- Klíčová pro zdvojnásobení kapacity hovorů v síti GSM ve srovnání s Full Rate

## Definující specifikace

- **TS 46.020** (Rel-19) — GSM Half Rate Speech Codec Specification
- **TS 46.022** (Rel-19) — GSM Half Rate DTX Comfort Noise Specification
- **TS 46.042** (Rel-19) — GSM Half-Rate Voice Activity Detector Specification

---

📖 **Anglický originál a plná specifikace:** [AFLAT na 3GPP Explorer](https://3gpp-explorer.com/glossary/aflat/)
