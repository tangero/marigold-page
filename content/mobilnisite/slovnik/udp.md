---
slug: "udp"
url: "/mobilnisite/slovnik/udp/"
type: "slovnik"
title: "UDP – User Datagram Protocol"
date: 2025-01-01
abbr: "UDP"
fullName: "User Datagram Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/udp/"
summary: "Základní protokol transportní vrstvy poskytující nespojované, nespolehlivé datagramové služby pro IP sítě. Nabízí minimální režii bez navazování spojení, řazení nebo opakovaného přenosu, což jej činí"
---

UDP je základní protokol transportní vrstvy poskytující nespojované, nespolehlivé datagramové služby s minimální režií pro aplikace s nízkou latencí, jako je VoIP a streamování v reálném čase v IP sítích.

## Popis

User Datagram Protocol (UDP) je základní transportní protokol definovaný [IETF](/mobilnisite/slovnik/ietf/) ([RFC](/mobilnisite/slovnik/rfc/) 768) a široce přijatý ve specifikacích 3GPP pro IP komunikaci. Fungující na transportní vrstvě (vrstva 4) modelu [OSI](/mobilnisite/slovnik/osi/) poskytuje UDP jednoduchou, nespojovanou službu, která odesílá datagramy – samostatné pakety dat – bez předchozího navázání spojení nebo zaručení doručení. Každý UDP paket obsahuje hlavičku se zdrojovým a cílovým číslem portu, délkou a kontrolním součtem pro základní detekci chyb, ale postrádá mechanismy pro řazení, řízení toku nebo opakovaný přenos. Tento návrh vede k nízké režii a minimální latenci, protože pakety jsou přenášeny okamžitě bez vyjednávání, i když mohou dorazit mimo pořadí, být duplikovány nebo ztraceny bez upozornění.

V architekturách 3GPP je UDP využíván napříč četnými rozhraními a funkcemi, zejména tam, kde rychlost a efektivita převažují nad požadavky na spolehlivost. Například v IP Multimedia Subsystem (IMS) přenáší UDP mediální proudy v reálném čase pro hlasové a videohovory, často ve spojení s Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)). Také tvoří základ kritických protokolů řídicí roviny, jako je Domain Name System ([DNS](/mobilnisite/slovnik/dns/)) pro překlad adres a Dynamic Host Configuration Protocol ([DHCP](/mobilnisite/slovnik/dhcp/)) pro přidělování IP adres v mobilních sítích. Bezstavová povaha protokolu jej činí škálovatelným pro scénáře vysílání (broadcast) nebo skupinového vysílání (multicast), jako je tomu u služeb multimedia broadcast ([MBMS](/mobilnisite/slovnik/mbms/)), kde jediný přenos dosáhne více uživatelů bez individuálních spojení.

Role UDP se rozšiřuje na vzájemné propojování mezi sítěmi 3GPP a ne-3GPP, jako je Wi-Fi nebo pevný broadband, kde usnadňuje bezproblémovou IP konektivitu. V systémech 5G je UDP i nadále specifikováno pro přenos dat uživatelské roviny mezi síťovými funkcemi, zejména v kontextech edge computingu, kde je ultranízká latence prvořadá. Navzdory své jednoduchosti může být UDP vylepšeno mechanismy aplikační vrstvy – jako je dopředná korekce chyb nebo opakovaný přenos – pro splnění specifických požadavků na spolehlivost, jak je vidět u protokolů jako [QUIC](/mobilnisite/slovnik/quic/). Jeho rozšířené zařazení do specifikací 3GPP, od procedur jádra sítě po signalizaci přístupu k rádiu, podtrhuje jeho všestrannost jako stavebního kamene pro rozmanité služby, vyvažující výkon s flexibilitou pro implementaci spolehlivosti na vyšší vrstvě podle potřeby.

## K čemu slouží

UDP bylo vytvořeno pro naplnění potřeby lehkého transportního protokolu s nízkou latencí v IP sítích, řešící scénáře, kde je režie spojovaných protokolů jako TCP nepřijatelná. V rané datové komunikaci zavedla spolehlivé doručování TCP – dosahované handshake, potvrzeními a opakovanými přenosy – zpoždění a složitost nevhodnou pro aplikace v reálném čase nebo časově citlivé. Toto omezení se stalo kritickým s příchodem interaktivních služeb, jako je voice over IP (VoIP) a živé streamování videa, kde je včasný příchod datových paketů důležitější než dokonalá spolehlivost.

V rámci 3GPP bylo přijetí UDP hnací silou evoluce směrem k plně IP sítím, počínaje 3G UMTS a pokračujíc přes 4G LTE a 5G NR. Řeší problémy související s efektivním využitím zdrojů a rychlým přenosem dat, zejména v řídicí signalizaci a doručování médií. Například v telefonii založené na IMS umožňuje UDP rychlé navázání hlasových hovorů bez latence spojení TCP, zatímco v MBMS podporuje efektivní vysílání pro více zařízení. Jeho jednoduchost také snižuje procesní zátěž na síťových uzlech a uživatelských zařízeních, což je zásadní pro mobilní zařízení s omezenou kapacitou baterie. Tím, že poskytuje standardizovanou, minimalistickou transportní vrstvu, umožňuje UDP systémům 3GPP optimalizovat výkon pro širokou škálu aplikací, od signalizace s vysokou důležitostí až po datové proudy typu best-effort, a slouží jako základ pro specializovanější protokoly přizpůsobené specifickým požadavkům služeb.

## Klíčové vlastnosti

- Nespojovaný provoz bez fází navázání nebo ukončení spojení
- Minimální režie hlavičky (8 bajtů) pro efektivní přenos paketů
- Podpora skupinového (multicast) a hromadného (broadcast) vysílání pro komunikaci jeden–více
- Volitelný kontrolní součet pro základní detekci chyb v užitečném zatížení
- Bezstavový návrh umožňující vysokou škálovatelnost a nízkou latenci
- Široce používán jako podklad pro protokoly reálného času, jako je RTP a DNS

## Související pojmy

- [IP – IP Packet eXchange](/mobilnisite/slovnik/ip/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [DNS – Directory Name Service](/mobilnisite/slovnik/dns/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.468** (Rel-19) — Group Communication System Enablers for LTE
- **TS 23.849** (Rel-11) — Study on IMS Roaming Media Optimization
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- … a dalších 81 specifikací

---

📖 **Anglický originál a plná specifikace:** [UDP na 3GPP Explorer](https://3gpp-explorer.com/glossary/udp/)
