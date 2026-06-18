---
slug: "wmm"
url: "/mobilnisite/slovnik/wmm/"
type: "slovnik"
title: "WMM – Wi-Fi Multimedia"
date: 2025-01-01
abbr: "WMM"
fullName: "Wi-Fi Multimedia"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wmm/"
summary: "WMM je certifikace Wi-Fi Alliance založená na IEEE 802.11e, která poskytuje kvalitu služeb (QoS) pro sítě Wi-Fi. Priorizuje provoz do čtyř přístupových kategorií (hlas, video, best effort, pozadí) za"
---

WMM je certifikace Wi-Fi Alliance založená na IEEE 802.11e, která poskytuje kvalitu služeb (QoS) prostřednictvím prioritizace provozu do čtyř přístupových kategorií za účelem zlepšení výkonu pro aplikace citlivé na latenci v sítích Wi-Fi.

## Popis

Wi-Fi Multimedia (WMM) je podmnožinou standardu [IEEE](/mobilnisite/slovnik/ieee/) 802.11e, certifikovaná Wi-Fi Alliance pro zajištění interoperability. Zavádí Enhanced Distributed Channel Access (EDCA), funkci přístupu ke kanálu založenou na soutěžení, která poskytuje prioritní QoS. WMM negarantuje šířku pásma ani latenci, ale statisticky upřednostňuje provoz definicí čtyř přístupových kategorií ([AC](/mobilnisite/slovnik/ac/)): Voice (AC_VO), Video (AC_[VI](/mobilnisite/slovnik/vi/)), Best Effort (AC_BE) a Background (AC_BK). Každé AC je přiřazena jedinečná sada parametrů EDCA, včetně Arbitration Interframe Space Number (AIFSN), minima contention window (CWmin) a maxima contention window (CWmax). Tyto parametry určují pravděpodobnost a načasování přístupu ke kanálu, přičemž AC_VO má nejkratší čekací doby a nejvyšší prioritu pro vysílání, následované AC_VI, AC_BE a AC_BK.

Architektura funguje tak, že každá Wi-Fi stanice ([STA](/mobilnisite/slovnik/sta/)) implementuje čtyři nezávislé fronty pro vysílání, jednu pro každé AC. Provoz je směrován do těchto front na základě označení paketů, jako jsou IP [DSCP](/mobilnisite/slovnik/dscp/) nebo 802.1D User Priority tagy. Když je médium volné, musí stanice před spuštěním své odpočítávací procedury (backoff) počkat po dobu Arbitration Interframe Space (AIFS) specifickou pro její AC. Vyšší prioritní AC mají kratší hodnoty AIFS a menší contention windows, což jim dává vyšší statistickou pravděpodobnost získání přístupu ke kanálu oproti provozu s nižší prioritou. Tento mechanismus je plně distribuovaný a nevyžaduje centrálního koordinátora, což jej činí vhodným pro soutěživou povahu Wi-Fi.

V rámci architektury 3GPP je WMM specifikováno pro použití v důvěryhodných ne-3GPP přístupových sítích, jako je podniková nebo operátorská Wi-Fi, které se propojují s 3GPP jádrem přes rozhraní S2a založené na [GTP](/mobilnisite/slovnik/gtp/) nebo PMIPv6. Jeho úlohou je poskytovat základní diferenciaci provozu pro uživatelskou rovinu dat, když je UE připojeno přes Wi-Fi, a zajistit tak koexistenci služeb v reálném čase s přenosy dat na pozadí. Přestože není tak deterministický jako 3GPP QoS mechanismy, WMM je klíčovým prvkem pro hlas přes Wi-Fi (VoWiFi) a streamování videa v integrovaných 3GPP-Wi-Fi sítích a tvoří základní vrstvu pro QoS v heterogenních přístupových scénářích.

## K čemu slouží

WMM bylo vytvořeno, aby řešilo absenci nativní kvality služeb (QoS) ve standardních sítích Wi-Fi [IEEE](/mobilnisite/slovnik/ieee/) 802.11, které používaly jednoduchý [DCF](/mobilnisite/slovnik/dcf/) (Distributed Coordination Function) zacházející se vším provozem stejně a s přístupem 'kdo dřív přijde, ten dřív mele'. Tento model způsoboval výrazné zhoršení výkonu pro aplikace citlivé na latenci, jako je Voice over IP (VoIP) a streamování videa, protože tyto pakety musely neférově soutěžit s velkými stahováním souborů nebo provozem na pozadí, což vedlo k jitteru, zpoždění a ztrátě paketů. Wi-Fi Alliance přijalo a certifikovalo podmnožinu IEEE 802.11e, aby vytvořilo standardizovaný, interoperabilní QoS profil – WMM – který by mohl být široce implementován v koncových i podnikových zařízeních.

Motivace byla hnána rostoucí konvergencí celulárních a Wi-Fi sítí a potřebou spolehlivých multimediálních služeb v neregulovaném spektru. Když 3GPP začalo specifikovat propojení s ne-3GPP přístupem (nejprve v SAE/EPC), byl nezbytný standardizovaný způsob zpracování QoS na Wi-Fi spojích, aby byla zajištěna konzistentní uživatelská zkušenost při offloadu relací z celulární RAN. WMM poskytlo komerčně životaschopnou, široce podporovanou základní linii pro prioritizaci provozu bez nutnosti plné složitosti HCF (Hybrid Coordination Function) standardu 802.11e nebo rezervace prostředků. Vyřešilo problém, že 'best-effort' Wi-Fi není vhodné pro operátorské služby, a umožnilo vývoj plynulého pokračování hlasových a video hovorů mezi celulárními a Wi-Fi sítěmi.

## Klíčové vlastnosti

- Čtyři prioritní přístupové kategorie (AC): Voice, Video, Best Effort, Background
- Enhanced Distributed Channel Access (EDCA) pro statistickou prioritizaci provozu
- Parametrizovaný přístup ke kanálu pomocí AIFSN, CWmin a CWmax pro každé AC
- Klasifikace provozu na základě IP DSCP nebo 802.1D User Priority tagů
- Distribuovaný provoz bez centrální koordinace
- Certifikace Wi-Fi Alliance pro interoperabilitu

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [WLAN – Wireless Local Area Network](/mobilnisite/slovnik/wlan/)

## Definující specifikace

- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)

---

📖 **Anglický originál a plná specifikace:** [WMM na 3GPP Explorer](https://3gpp-explorer.com/glossary/wmm/)
