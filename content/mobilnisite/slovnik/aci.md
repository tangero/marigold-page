---
slug: "aci"
url: "/mobilnisite/slovnik/aci/"
type: "slovnik"
title: "ACI – Adjacent Channel Interference"
date: 2025-01-01
abbr: "ACI"
fullName: "Adjacent Channel Interference"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/aci/"
summary: "Adjacent Channel Interference (ACI, rušení sousedním kanálem) je degradace kvality rádiového signálu způsobená přeléváním energie z přenosu v jednom kmitočtovém kanálu do sousedního kanálu. Jde o klíč"
---

ACI je degradace kvality rádiového signálu způsobená přeléváním energie z přenosu v jednom kmitočtovém kanálu do sousedního kanálu, což omezuje výkon v celulárních sítích.

## Popis

Adjacent Channel Interference (ACI, rušení sousedním kanálem) je forma ko-kanálového rušení specifická pro kmitočtovou doménu. Vzniká v důsledku neideálních charakteristik rádiových vysílačů a přijímačů. V ideálním systému by vysílač vyzařoval energii dokonale omezenou na přidělenou šířku pásma kanálu a přijímač by zachycoval energii pouze z tohoto přesného kanálu. Ve skutečnosti vysílače produkují nežádoucí vyzařování mimo pásmo ([OOBE](/mobilnisite/slovnik/oobe/)), které se šíří do sousedních kanálů, a přijímače mají konečnou selektivitu, což znamená, že mohou být ovlivněny silnými signály v sousedních kanálech. Toto nežádoucí přelévání energie způsobuje rušení, které degraduje poměr signálu k rušení a šumu (SINR) pro požadovaný signál. Závažnost ACI závisí na několika faktorech, včetně vysílacího výkonu, spektrální masky (nebo poměru úniku do sousedního kanálu, [ACLR](/mobilnisite/slovnik/aclr/)) vysílače, selektivity sousedního kanálu ([ACS](/mobilnisite/slovnik/acs/)) přijímače a odstupu kanálů mezi přidělenými nosnými.

Z architektonické a provozní perspektivy je řízení ACI základním aspektem správy rádiových zdrojů (RRM) a plánování sítě. Mezi klíčové komponenty zapojené do tohoto procesu patří uživatelské zařízení (UE) a základnová stanice (eNodeB v LTE, gNB v NR), přičemž pro každou jsou ve specifikacích 3GPP definovány požadavky na výkon vysílače a přijímače. Operátor sítě musí pečlivě plánovat přidělování kmitočtů s ohledem na ochranná pásma a uspořádání kanálů, aby ACI zmírnil. Například ve scénářích agregace nosných jsou definovány specifické kombinace komponentních nosných, aby bylo zajištěno, že agregované nosné mají dostatečný odstup nebo jsou nakonfigurovány s řízením výkonu pro omezení vzájemného rušení.

Role ACI v síti přímo souvisí se spektrální účinností a kapacitou. Neřízené ACI nutí síť pracovat s vyšší interferenční rezervou, což snižuje použitelný modulační a kódovací schéma ([MCS](/mobilnisite/slovnik/mcs/)), a tím i propustnost pro uživatele. V hustých nasazeních, jako jsou small buňky nebo in-band nasazení různých technologií (např. LTE a NR sdílejících spektrum), se ACI stává primárním problémem. Proto specifikace 3GPP definují přísné požadavky na ACLR a ACS, aby bylo zajištěno, že zařízení od různých výrobců mohou koexistovat bez nadměrného vzájemného rušení. K udržení ACI v přijatelných mezích se používají techniky jako řízení výkonu, pokročilá filtrace a pečlivé kmitočtové plánování, což síti umožňuje využívat dostupné spektrum co nejefektivněji.

## K čemu slouží

ACI existuje jako základní fyzikální omezení ve všech rádiových komunikačních systémech. Účelem definování a standardizace jeho parametrů (jako [ACLR](/mobilnisite/slovnik/aclr/) a [ACS](/mobilnisite/slovnik/acs/)) v rámci 3GPP je zajistit interoperabilitu mezi síťovými zařízeními od různých výrobců a umožnit předvídatelný výkon sítě. Bez takových standardizovaných limitů by základnová stanice nebo mobilní zařízení jednoho výrobce mohlo způsobit ochromující rušení zařízení jiného výrobce pracujícímu na sousedním kanálu, což by vedlo k výpadkům sítě a špatnému uživatelskému zážitku. Tento koncept řeší problém konečného spektra – s rostoucí poptávkou po mobilních datech musí operátoři spektrum využívat intenzivněji, umisťovat kanály blíže k sobě, což inherentně zvyšuje potenciál pro ACI.

Historicky, jak se celulární technologie vyvíjely od GSM (s 200 kHz kanály) přes UMTS (5 MHz) až k LTE a 5G NR (s škálovatelnými šířkami pásma až do 100 MHz), se výzva ACI stala výraznější. Širší pásma a modulační schémata vyššího řádu (jako 256QAM a 1024QAM) jsou na rušení citlivější. Omezení předchozích přístupů se často řešila použitím větších ochranných pásem, což je však neefektivní využití vzácného spektra. Motivací pro přísnou specifikaci ACI a techniky jeho potlačení je minimalizace těchto ochranných pásem, a tím maximalizace využitelného spektra pro vlastní přenos dat. To zvyšuje kapacitu sítě a přenosové rychlosti ve stejném licencovaném kmitočtovém bloku, což je klíčový ekonomický a technický cíl provozovatelů mobilních sítí.

## Klíčové vlastnosti

- Definováno nežádoucím vyzařováním vysílače mimo pásmo (OOBE) a poměrem úniku do sousedního kanálu (ACLR)
- Řízeno výkonem selektivity sousedního kanálu (ACS) přijímače
- Kritické pro koexistenci zařízení mezi operátory a různými výrobci
- Přímo ovlivňuje dosažitelnou spektrální účinnost a kapacitu sítě
- Řízeno prostřednictvím plánování sítě, přidělování kmitočtů a ochranných pásem
- Klíčový aspekt ve scénářích agregace nosných a sdílení spektra

## Související pojmy

- [ACLR – Adjacent Channel Leakage Power Ratio](/mobilnisite/slovnik/aclr/)
- [ACS – Auto-Configuration Server](/mobilnisite/slovnik/acs/)

## Definující specifikace

- **TR 38.828** (Rel-16) — CLI and RIM for NR
- **TR 45.903** (Rel-19) — SAIC Feasibility Study for GSM Networks
- **TR 45.913** (Rel-19) — Optimized Transmit Pulse Shape for EGPRS2-B
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [ACI na 3GPP Explorer](https://3gpp-explorer.com/glossary/aci/)
