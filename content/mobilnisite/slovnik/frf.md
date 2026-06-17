---
slug: "frf"
url: "/mobilnisite/slovnik/frf/"
type: "slovnik"
title: "FRF – Frequency Reuse Factor"
date: 2025-01-01
abbr: "FRF"
fullName: "Frequency Reuse Factor"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/frf/"
summary: "Metrika síťového plánování, která definuje, jak často je stejný frekvenční kanál znovu použit v různých buňkách celulárního systému. Je to klíčový parametr pro řízení interference a spektrální účinnos"
---

FRF je metrika síťového plánování, která definuje, jak často je stejný frekvenční kanál znovu použit v různých buňkách, a řídí tak interferenci a spektrální účinnost v celulárním systému.

## Popis

Faktor opakovaného využití frekvence (FRF) je základním konceptem v návrhu celulárních sítí a představuje převrácenou hodnotu počtu buněk v clusteru, které sdílejí celkové dostupné frekvenční spektrum. V klasickém hexagonálním uspořádání buněk je celková dostupná šířka pásma rozdělena na sadu ortogonálních frekvenčních kanálů. Tyto kanály jsou pak rozděleny mezi cluster N buněk, přičemž žádný kanál není v rámci stejného clusteru znovu použit, aby se zabránilo ko-kanálové interferenci. FRF je matematicky definován jako 1/N. Nižší FRF (např. 1/1 nebo 1/3) označuje agresivnější vzor opakovaného využití, který umožňuje použít stejnou frekvenci ve více buňkách, což zvyšuje celkovou kapacitu, ale také zvyšuje potenciál pro interferenci mezi buňkami používajícími stejnou frekvenci. Naopak vyšší FRF (např. 1/7) znamená, že frekvence jsou znovu používány méně často na větší geografické oblasti, což snižuje interferenci, ale také omezuje kapacitu na jednotku plochy.

Síťové plánování zahrnuje výběr optimálního FRF na základě tolerance systému k interferenci, která je dána požadavkem na poměr nosná-interference ([CIR](/mobilnisite/slovnik/cir/)). Velikost clusteru N určuje minimální vzdálenost mezi buňkami používajícími stejnou frekvenci, známou jako ko-kanálová vzdálenost pro opakované využití. Tato vzdálenost musí být dostatečná k zajištění, že signál z obsluhující buňky je dostatečně silný ve srovnání s rušivými signály z jiných buněk používajících stejnou frekvenci. Volba N a odpovídajícího FRF je kritický kompromis. Rané sítě GSM často používaly větší velikosti clusterů (např. N=7 nebo 4) s vyššími FRF, aby zajistily kvalitu hovoru v prostředí omezeném interferencí. Moderní sítě LTE a 5G NR s pokročilými technikami, jako je ortogonální multiplex s frekvenčním dělením s více přístupem ([OFDMA](/mobilnisite/slovnik/ofdma/)), koordinace interference ([ICIC](/mobilnisite/slovnik/icic/)/eICIC) a sofistikované řízení výkonu, mohou efektivně fungovat s mnohem nižšími FRF, například 1/1 (univerzální opakované využití frekvence), čímž maximalizují spektrální účinnost.

FRF není statický parametr konfigurovaný v uživatelském zařízení, ale plánovací princip uplatňovaný operátory sítí. Ovlivňuje nasazení základnových stanic, sklon antény a nastavení výkonu. Ve spojení se sektorizací a použitím vícevstupních/výstupních ([MIMO](/mobilnisite/slovnik/mimo/)) antén je plánování FRF součástí holistické strategie rádiových frekvencí (RF). Pro 5G, zejména v hustých městských nasazeních, síťové slicing a dynamické sdílení spektra dále komplikují tradiční statický pohled na FRF, což vede k adaptivnějším a softwarově definovaným přístupům k řízení interference. Nicméně základní koncept zůstává klíčový pro pochopení základních limitů a návrhových voleb rádiové přístupové sítě (RAN) jakékoli celulární sítě.

## K čemu slouží

Hlavním účelem definování a optimalizace faktoru opakovaného využití frekvence je umožnit efektivní využití vzácného a licencovaného rádiového spektra k obsluze velkého počtu uživatelů na rozsáhlé geografické oblasti. Bez opakovaného využití frekvence by celulární síť nebyla možná, protože by vyžadovala jedinečnou frekvenci pro každou buňku, což by téměř okamžitě vyčerpalo dostupné spektrum. Koncept celulární architektury, poprvé představený v éře 1G, je zásadně založen na opakovaném využití frekvencí v geograficky oddělených buňkách za účelem znásobení kapacity sítě.

Historicky měly rané analogové systémy (1G) omezené možnosti pro potlačení interference, což vyžadovalo velké velikosti clusterů (např. N=7) a vysoké FRF pro udržení přijatelné kvality hovoru, což výrazně omezovalo kapacitu. Přechod na digitální standardy jako GSM (2G) umožnil robustnější modulaci a korekci chyb, což umožnilo těsnější vzory opakovaného využití (např. N=4 nebo 3). Evoluce k 3G (UMTS) s širokopásmovým vícečetným přístupem s kódovým dělením (WCDMA) zavedla paradigma univerzálního opakovaného využití frekvence (FRF=1) v rámci sítě stejného operátora, spoléhající se na rozprostírací kódy a řízení výkonu pro správu interference, což byl významný posun od tvrdého dělení frekvencí.

Současný tlak na vyšší přenosové rychlosti a kapacitu v sítích 4G LTE a 5G NR žene sítě k ještě agresivnějšímu opakovanému využití, často s cílem dosáhnout FRF=1 ve všech sektorech. To je umožněno pokročilými technologiemi fyzické vrstvy, jako je [OFDMA](/mobilnisite/slovnik/ofdma/), která poskytuje inherentní odolnost vůči některým interferencím, a sofistikovanými síťovými technikami koordinace a potlačení interference. Koncept FRF tedy řeší základní ekonomický a technický problém nedostatku spektra a jeho vývoj odráží neustálé zlepšování odvětví v řízení kompromisu mezi interferencí a kapacitou.

## Klíčové vlastnosti

- Definuje převrácenou hodnotu velikosti clusteru (N) pro frekvenční plánování
- Přímo ovlivňuje úroveň ko-kanálové interference v síti
- Základní kompromisní parametr mezi kapacitou systému a kvalitou signálu
- Určuje minimální vzdálenost pro opakované využití mezi buňkami používajícími stejnou frekvenci
- Statická plánovací metrika, která je základem architektury celulární sítě
- Jeho optimální hodnota závisí na modulačním schématu, anténní technologii a toleranci k interferenci

## Definující specifikace

- **TR 37.911** (Rel-19) — 3GPP 5G NTN Self-Evaluation Report
- **TS 38.821** (Rel-16) — NR Support for Non-Terrestrial Networks
- **TS 38.863** (Rel-19) — NR NTN RF and Co-existence Spec
- **TS 48.014** (Rel-19) — Gb Interface Physical Layer Specification
- **TS 48.016** (Rel-19) — Gb Interface Network Service Specification

---

📖 **Anglický originál a plná specifikace:** [FRF na 3GPP Explorer](https://3gpp-explorer.com/glossary/frf/)
