---
slug: "vbrp"
url: "/mobilnisite/slovnik/vbrp/"
type: "slovnik"
title: "VBRP – Variable Bit Rate Packet transmission"
date: 2025-01-01
abbr: "VBRP"
fullName: "Variable Bit Rate Packet transmission"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vbrp/"
summary: "VBRP je metoda přenosu paketů pro multimediální služby, která podporuje proměnlivý datový tok a umožňuje efektivnější využití síťových zdrojů ve srovnání s přenosem s konstantním datovým tokem. Je klí"
---

VBRP je metoda přenosu paketů pro multimediální služby, která podporuje proměnlivý datový tok, což umožňuje efektivnější využití síťových zdrojů než přenos s konstantním datovým tokem u adaptivních mediálních proudů.

## Popis

Přenos paketů s proměnlivým datovým tokem (Variable Bit Rate Packet - VBRP) je základním konceptem ve specifikacích 3GPP pro zpracování multimediálního provozu přes paketově přepínané sítě, zejména v kontextu služby Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a dalších streamovacích služeb. Na rozdíl od přenosu s konstantním datovým tokem ([CBR](/mobilnisite/slovnik/cbr/)), který alokuje pevnou šířku pásma bez ohledu na složitost obsahu, VBRP dynamicky přizpůsobuje přenosovou rychlost na základě okamžitých požadavků kódovaného média. Toho je dosaženo paketizací mediálních proudů kódovaných s proměnlivým datovým tokem, jako jsou ty produkované kodeky typu H.264/[AVC](/mobilnisite/slovnik/avc/) nebo [AMR-WB](/mobilnisite/slovnik/amr-wb/), do IP paketů pro přenos přes core síť a rádiovou přístupovou síť. Síť musí tyto pakety s proměnnou rychlostí spravovat a zajistit jejich doručení s odpovídajícími parametry kvality služby (QoS), včetně přípustného zpoždění, jitteru a ztráty paketů, aby byla zachována přijatelná uživatelská zkušenost.

Architektura podporující VBRP zahrnuje několik klíčových komponent v systému 3GPP. Na aplikační vrstvě mediální servery nebo centra pro broadcast/multicast služby generují obsah kódovaný s proměnným datovým tokem ([VBR](/mobilnisite/slovnik/vbr/)). Core síť, včetně Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) a Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)), zajišťuje směrování paketů, označování QoS (např. pomocí QoS Class Identifiers) a případně ukládání obsahu do cache. V rádiové přístupové síti (RAN) základnové stanice (eNodeB v LTE, gNB v 5G NR) naplánují tyto pakety s proměnnou rychlostí přes rozhraní, přičemž využívají techniky adaptace spoje, jako je Adaptive Modulation and Coding ([AMC](/mobilnisite/slovnik/amc/)), aby odpovídaly rádiovým podmínkám. Dynamická povaha provozu VBRP vyžaduje sofistikované řízení rádiových zdrojů, aby se zabránilo přetížení a zároveň maximalizovala spektrální efektivita, zejména během období špičkového datového toku mediálního proudu.

Role VBRP je nedílnou součástí efektivního doručování multimédií. Umožňuje síti statisticky multiplexovat více VBR proudů a využívat skutečnosti, že ne všechny proudy současně vyžadují špičkovou šířku pásma. To vede k vyšší celkové využitelnosti sítě ve srovnání s dimenzováním na špičkové CBR rychlosti. Pro koncové uživatelské zařízení přenos VBRP vyžaduje vyrovnávací paměť pro přehrávání (playout buffer), která absorbuje variabilitu v časech příchodu paketů a vyhladí přehrávání. Specifikace 3GPP, zejména v TS 26.937, definují protokoly a procedury pro přenos VBRP proudů, čímž zajišťují interoperabilitu mezi různými síťovými elementy a zařízeními od výrobců. Jeho implementace je klíčovým prvkem pro poskytování šetrných k šířce pásma a vysoce kvalitních video a hlasových služeb v moderních mobilních sítích.

## K čemu slouží

VBRP bylo zavedeno, aby řešilo neefektivitu přenosu multimediálního obsahu metodami s konstantním datovým tokem (CBR) přes paketově přepínané sítě. Předchozí přístupy, často odvozené od telefonie s přepojováním okruhů, alokovaly pevný kanál šířky pásma bez ohledu na skutečný informační obsah mediálního snímku. Pro video, které má přirozeně vysokou variabilitu ve složitosti scény (např. statická scéna vs. scéna s rychlým pohybem), je přenos CBR plýtvavý během jednoduchých scén a degradační pro kvalitu během složitých scén, protože enkodér musí uměle omezit detaily, aby se vešel do pevného datového rozpočtu.

Vytvoření VBRP bylo motivováno přechodem k IP multimediálním službám (IMS) a potřebou efektivního využití jak core síťových přenosových tras, tak vzácného rádiového spektra. Tím, že umožňuje přenášenému datovému toku se měnit podle výstupu zdrojového enkodéru, VBRP umožňuje konzistentní, vysokou percepční kvalitu. Řeší problém neefektivního využití šířky pásma a umožňuje operátorům obsloužit více uživatelů nebo poskytovat proudy vyšší kvality ve stejném síťovém kapacitním rámci. To bylo obzvláště kritické pro ekonomickou životaschopnost služeb náročných na šířku pásma, jako je mobilní TV a streamování videa, zavedených v časovém rámci 3GPP Rel-8 a později.

Historicky VBRP navázalo na koncepty z pevné linky pro video kódování a internetového streamování a přizpůsobilo je jedinečným výzvám mobilních sítí, jako jsou proměnlivé rádiové podmínky a handovery. Řešilo omezení dřívějších mobilních multimediálních služeb, které byly buď nízké kvality, nebo neúměrně nákladné z hlediska síťových zdrojů. VBRP se spolu s pokročilými video kodeky stalo základním kamenem pro poskytování služeb zaměřených na video, které definují moderní uživatelské zážitky v 4G a 5G.

## Klíčové vlastnosti

- Dynamická adaptace šířky pásma na základě složitosti mediálního obsahu
- Efektivní statistické multiplexování více mediálních proudů
- Podpora pokročilých video a audio kodeků (např. H.264, HEVC, EVS)
- Integrace s rámcem QoS 3GPP pro prioritní zpracování paketů
- Vyžaduje vyrovnávací paměť pro přehrávání (playout buffer) na přijímací straně pro zajištění plynulého přehrávání
- Kompatibilní s režimy doručování unicast i multicast/broadcast (MBMS)

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 26.937** (Rel-19) — 3GPP PSS Characterization

---

📖 **Anglický originál a plná specifikace:** [VBRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/vbrp/)
