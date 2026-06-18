---
slug: "sc-vbr"
url: "/mobilnisite/slovnik/sc-vbr/"
type: "slovnik"
title: "SC-VBR – Source Controlled Variable Bit Rate"
date: 2025-01-01
abbr: "SC-VBR"
fullName: "Source Controlled Variable Bit Rate"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sc-vbr/"
summary: "Metoda kódování a přenosu médií, při níž zdroj (např. video enkodér) mění svůj výstupní datový tok na základě složitosti obsahu a je tato variabilita signalizována síti. Umožňuje vyšší kvalitu pro slo"
---

SC-VBR je metoda kódování médií, při níž zdroj mění svůj výstupní datový tok na základě složitosti obsahu, přičemž je tato variabilita signalizována síti za účelem vyvážení kvality a efektivity využití šířky pásma v rámci garantovaného rozsahu.

## Popis

Source Controlled Variable Bit Rate (SC-VBR) je profil pro doručování médií definovaný v rámci architektur služby paketového streamování ([PSS](/mobilnisite/slovnik/pss/)) a služby multimediálního vysílání a skupinového vysílání ([MBMS](/mobilnisite/slovnik/mbms/)) konsorcia 3GPP. Jedná se o specifický provozní režim pro video a audio kodeky, kdy enkodér negeneruje konstantní datový tok ([CBR](/mobilnisite/slovnik/cbr/)), ale místo toho umožňuje, aby se datový tok měnil podle inherentní složitosti a pohybu ve zdrojovém obsahu. Zásadní je, že tato variabilita není libovolná; je 'řízena zdrojem', což znamená, že mediální server nebo enkodér definuje a signalizuje charakteristiky této variability klientovi a síti. To je v protikladu k neomezenému proměnnému datovému toku ([VBR](/mobilnisite/slovnik/vbr/)), který nemusí poskytovat předvídatelné požadavky na síťové zdroje.

Technické fungování SC-VBR se řídí parametry signalizovanými v popisu relace, typicky pomocí protokolu pro popis relace ([SDP](/mobilnisite/slovnik/sdp/)). Klíčové parametry zahrnují 'maximumBitrate' a 'averageBitrate'. Enkodér generuje datový tok, kde okamžitý datový tok může kolísat až do hodnoty 'maximumBitrate', ale dlouhodobý průměr nepřekročí hodnotu 'averageBitrate'. Síť může tyto parametry použít pro řízení přístupu a rezervaci zdrojů. Například ve spravovaném přenosu IP Multimedia Subsystem (IMS) nebo MBMS může síť rezervovat zdroje na základě 'maximumBitrate', aby garantovala kvalitu bez ztráty paketů během scén s vrcholnou složitostí, zatímco statistického multiplexování lze dosáhnout napříč více datovými toky, protože ne všechny toky budou vrcholit současně.

Z architektonického hlediska zahrnuje SC-VBR komponenty napříč řetězcem přípravy obsahu, doručování a spotřeby. Na straně přípravy obsahu mediální server (např. PSS server) zakóduje obsah pomocí SC-VBR profilu kodeku jako je H.264/[AVC](/mobilnisite/slovnik/avc/) nebo H.265/[HEVC](/mobilnisite/slovnik/hevc/) a vygeneruje odpovídající popis mediální prezentace (např. soubor .3gp s příslušnými hlavičkami stop). Doručovací síť, což může být 3GPP [PS](/mobilnisite/slovnik/ps/) síť s vyhrazenými přenosy nebo vysílací síť jako MBMS, přijímá parametry popisu relace. Rámec řízení politiky a účtování (PCC) sítě může tyto parametry interpretovat pro zřízení vhodného přenosu s garantovaným datovým tokem (GBR). Nakonec klientské zařízení (UE) přijme SDP popis, porozumí modelu variability datového toku a může podle toho přizpůsobit správu své vyrovnávací paměti pro přehrávání. Toto koncově uvědomělé řízení variability umožňuje konzistentní kvalitu uživatelského prožitku (QoE), protože složité scény dostávají více bitů pro zachování čistoty, zatímco jednoduché scény používají méně bitů, čímž uvolňují síťovou kapacitu pro ostatní uživatele nebo služby.

## K čemu slouží

SC-VBR byl vyvinut, aby překlenul propast mezi efektivitou využití šířky pásma čistého kódování s proměnným datovým tokem (VBR) a řiditelností konstantních datových toků (CBR) pro síť v případě služeb streamování v reálném čase přes 3GPP sítě. Tradiční CBR kódování vynucuje konstantní datový tok bez ohledu na obsah, což často vede ke snížené kvalitě během složitých scén (např. akčních sekvencí) nebo plýtvání bity během jednoduchých scén (např. záběr moderátora zpráv). Čistý VBR, ačkoli je z hlediska kvality optimální, vytváří datový tok s nepředvídatelnými špičkovými rychlostmi, což síti ztěžuje provádění řízení přístupu a rezervaci zdrojů, což může vést k přetížení, ztrátě paketů a zhoršenému uživatelskému prožitku.

Vytvoření SC-VBR bylo motivováno potřebou efektivního a kvalitního mobilního video streamování. Jak se služby 3GPP vyvíjely a zahrnovaly bohaté multimédia (PSS) a vysílání (MBMS), byla vyžadována metoda pro doručování vysoké vizuální kvality v rámci omezených a sdílených rádiových zdrojů mobilní sítě. SC-VBR to řeší tím, že poskytovateli obsahu dává řízenou variabilitu. Síť je informována o mezích této variability (maximální a průměrné rychlosti), což jí umožňuje plánovat přidělování zdrojů přesněji než u neomezeného VBR, a přitom efektivněji než u CBR. To bylo obzvláště důležité pro vysílací režim MBMS, kde statistické multiplexování více SC-VBR datových toků přes společný vysílací kanál může vést k významným úsporám šířky pásma ve srovnání s alokací špičkové rychlosti pro každý CBR datový tok. Řešilo to omezení dřívějších přístupů ke streamování, které buď kompromitovaly kvalitu (CBR), nebo představovaly výzvy pro síťové plánování (VBR), a umožnilo tak optimálnější kompromis pro komerční streamovací služby.

## Klíčové vlastnosti

- Datový tok se mění na základě složitosti zdrojového obsahu
- Definované parametry maximálního a průměrného datového toku jsou signalizovány síti
- Umožňuje konzistentní vizuální kvalitu přidělováním více bitů složitým scénám
- Umožňuje síti provádět informované řízení přístupu a rezervaci zdrojů
- Usnadňuje statistické multiplexování ve scénářích vysílání (MBMS)
- Specifikováno pro použití se službami streamování 3GPP PSS a MBMS

## Související pojmy

- [PSS – Packet Switched Streaming Service](/mobilnisite/slovnik/pss/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [SDP – Service Discovery Protocol](/mobilnisite/slovnik/sdp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.441** (Rel-19) — EVS Audio Processing Introduction
- **TS 26.442** (Rel-19) — EVS Codec Fixed Point ANSI-C Code
- **TS 26.443** (Rel-19) — EVS Codec Floating-Point C Code
- **TS 26.444** (Rel-19) — EVS Codec Conformance Test Sequences
- **TS 26.450** (Rel-19) — EVS Codec DTX System Level Aspects
- **TS 26.451** (Rel-19) — EVS Codec Voice Activity Detector (VAD) Specification
- **TS 26.452** (Rel-19) — EVS Codec Fixed-Point C Code Implementation
- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization

---

📖 **Anglický originál a plná specifikace:** [SC-VBR na 3GPP Explorer](https://3gpp-explorer.com/glossary/sc-vbr/)
