---
slug: "o-bcsm"
url: "/mobilnisite/slovnik/o-bcsm/"
type: "slovnik"
title: "O-BCSM – Originating Basic Call State Model"
date: 2025-01-01
abbr: "O-BCSM"
fullName: "Originating Basic Call State Model"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/o-bcsm/"
summary: "Model konečného automatu používaný v CAMELu (Customised Applications for Mobile networks Enhanced Logic) k definování a řízení sledu událostí pro odchozí (originating) hovor. Umožňuje síti aplikovat i"
---

O-BCSM je model konečného automatu používaný v CAMELu k definování a řízení sledu událostí pro odchozí hovor, který umožňuje inteligentní služby, jako je předplacené účtování, prostřednictvím interakce v určitých detekčních bodech.

## Popis

Originating Basic Call State Model (O-BCSM) je klíčovou součástí servisní architektury [CAMEL](/mobilnisite/slovnik/camel/) (Customised Applications for Mobile networks Enhanced Logic), definovanou jako konečný automat ([FSM](/mobilnisite/slovnik/fsm/)), který modeluje průběh odchozího hovoru iniciovaného z mobilního zařízení. Nachází se ve funkci Service Control Function ([SCF](/mobilnisite/slovnik/scf/)) a komunikuje s funkcí Service Switching Function ([SSF](/mobilnisite/slovnik/ssf/)) v mobile switching center ([MSC](/mobilnisite/slovnik/msc/)) nebo [GMSC](/mobilnisite/slovnik/gmsc/). Model se skládá z řady propojených stavů hovoru, jako jsou 'Authorize_Origination_Attempt', 'Collect_Information', 'Analyze_Information', 'Routing_&_Alerting' a 'Active'. Na klíčových přechodech mezi těmito stavy, známých jako detekční body (DPs), může SSF pozastavit zpracování hovoru a požádat o instrukce od SCF. To umožňuje servisní logice CAMEL, umístěné na vyhrazeném Service Control Point ([SCP](/mobilnisite/slovnik/scp/)), ovlivnit hovor – například změnou volaného čísla, aplikací účtování nebo zamítnutím hovoru na základě logiky specifické pro účastníka.

Fungování O-BCSM je řízeno událostmi. Když mobilní účastník zahájí hovor, MSC/SSF aktivuje O-BCSM a začne procházet jeho stavy. V každém nakonfigurovaném [DP](/mobilnisite/slovnik/dp/) SSF vyhodnotí, zda je tento bod aktivován pro notifikaci. Pokud je aktivován, odešle zprávu SCF obsahující podrobnosti o hovoru. SCF poté provede svou servisní logiku a vrátí odpověď, která může být instrukce 'Continue' pro pokračování v běžném zpracování hovoru, 'Request Report' pro monitorování dalších událostí nebo specifický příkaz jako 'Connect' či 'ReleaseCall'. Tato interakce je standardizována prostřednictvím protokolu CAMEL Application Part (CAP). Přesná definice O-BCSM zajišťuje konzistentní chování služeb napříč různými síťovými dodavateli a operátory.

Architektura modelu je navržena pro flexibilitu a kontrolu. Zahrnuje dva typy detekčních bodů: Trigger Detection Points (TDPs), které jsou staticky nakonfigurovány v profilu účastníka (O-CSI) a aktivovány při sestavování hovoru, a Event Detection Points (EDPs), které mohou být dynamicky aktivovány SCF během dialogu. To umožňuje jak předdefinované servisní spouštěče, tak dynamické interakce se službami během hovoru. O-BCSM se striktně zabývá pouze řídicí rovinou hovoru (call control plane); nezpracovává vlastní přenosovou cestu pro hlas. Jeho primární rolí je poskytnout standardizovaný rámec, ve kterém SSF hlásí události hovoru a SCF může vykonávat kontrolu, což umožňuje vytváření komplexních, síťových inteligentních služeb bez nutnosti úprav na straně koncového zařízení.

## K čemu slouží

O-BCSM byl vytvořen, aby poskytl standardizovaný, na dodavateli nezávislý model pro implementaci služeb inteligentní sítě (IN) v sítích GSM a UMTS, konkrétně pro hovory iniciované z mobilního zařízení. Před zavedením CAMELu a modelů jako O-BCSM byly pokročilé telefonní služby (jako bezplatná čísla nebo virtuální privátní sítě) z velké části pevně zabudovány do softwaru ústředny, což ztěžovalo jejich vytváření, úpravy nebo přenositelnost mezi různými dodavateli síťového vybavení. Tento nedostatek flexibility bránil rychlému nasazování služeb a inovacím.

O-BCSM jako součást rámce CAMEL to řeší oddělením servisní logiky od přepínací infrastruktury. Umožňuje operátorům hostovat služby na centralizovaných, škálovatelných SCP, které mohou řídit hovory v jakékoli MSC prostřednictvím interakce se standardizovaným stavovým modelem. To umožňuje vytváření služeb specifických pro účastníka a pracujících v reálném čase, jako je předplacené účtování, filtrování hovorů, překlad čísel nebo směrování na základě polohy. Definice konkrétních detekčních bodů v modelu poskytuje jasnou smlouvu mezi ústřednou a servisní logikou, což zajišťuje spolehlivé a předvídatelné provádění služeb.

Jeho zavedení v 3GPP Release 4 byl klíčovým krokem ve vývoji mobilních sítí od základní hlasové telefonie k programovatelným servisním platformám. Reagoval na obchodní potřebu operátorů se odlišovat pomocí vlastních služeb a implementovat komplexní schémata účtování, jako je předplacené, což byl hlavní faktor růstu mobilní penetrace v mnoha trzích. O-BCSM poskytl nezbytný řídicí mechanismus, který učinil tyto obchodní modely technicky proveditelnými ve velkém měřítku.

## Klíčové vlastnosti

- Standardizovaný konečný automat pro modelování průběhu odchozího hovoru
- Definuje konkrétní detekční body (DPs) pro interakci se SCF
- Podporuje jak Trigger Detection Points (TDPs), tak Event Detection Points (EDPs)
- Umožňuje řízení v reálném čase pro každý hovor externí servisní logikou (SCP)
- Umožňuje služby jako předplacené účtování, filtrování hovorů a překlad čísel
- Pro komunikaci mezi SSF a SCF využívá protokol CAP

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [T-BCSM – Terminating Basic Call State Model](/mobilnisite/slovnik/t-bcsm/)
- [O-CSI – Originating CAMEL Subscription Information](/mobilnisite/slovnik/o-csi/)
- [SCF – Service Control Function (IN context), Service Capability Feature (VHE/OSA context)](/mobilnisite/slovnik/scf/)
- [SSF – Service Switching Function](/mobilnisite/slovnik/ssf/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [O-BCSM na 3GPP Explorer](https://3gpp-explorer.com/glossary/o-bcsm/)
