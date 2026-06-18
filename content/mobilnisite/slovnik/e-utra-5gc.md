---
slug: "e-utra-5gc"
url: "/mobilnisite/slovnik/e-utra-5gc/"
type: "slovnik"
title: "E-UTRA/5GC – E-UTRA connected to 5G Core network"
date: 2025-01-01
abbr: "E-UTRA/5GC"
fullName: "E-UTRA connected to 5G Core network"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-utra-5gc/"
summary: "Provozní režim, ve kterém je přístupová síť 4G LTE (E-UTRA) připojena k nové síti 5G Core (5GC). To umožňuje LTE poskytovat služby využívající cloud-nativní, službami založenou architekturu 5G a umožň"
---

E-UTRA/5GC je provozní režim, ve kterém je přístupová síť 4G LTE (E-UTRA) připojena k síti 5G Core, což umožňuje LTE poskytovat služby využívající architekturu 5G pro plynulou migraci.

## Popis

[E-UTRA](/mobilnisite/slovnik/e-utra/)/5GC je klíčová konfigurace nasazení zavedená ve specifikaci 3GPP Release 15, kde je stávající přístupová síť Evolved Universal Terrestrial Radio Access (E-UTRA) – rádiová technologie pro 4G LTE – připojena k nové síti 5G Core (5GC). Tato architektura odděluje rádiovou přístupovou technologii od páteřní sítě, což umožňuje starším LTE rádiím poskytovat služby přes pokročilou, cloud-nativní 5GC. V tomto režimu se LTE eNodeB ([eNB](/mobilnisite/slovnik/enb/)) připojuje k 5GC přes rozhraní [NG](/mobilnisite/slovnik/ng/) (konkrétně NG-eNB se připojuje k funkci [AMF](/mobilnisite/slovnik/amf/) (Access and Mobility Management Function) a [UPF](/mobilnisite/slovnik/upf/) (User Plane Function)). Signalizace řídicí roviny mezi eNB a AMF používá protokol [NGAP](/mobilnisite/slovnik/ngap/), zatímco data uživatelské roviny proudí přes rozhraní N3 k UPF. Toto uspořádání umožňuje LTE uživatelským zařízením (UE) registrovat se a navazovat [PDU](/mobilnisite/slovnik/pdu/) (Packet Data Unit) relace s 5GC, čímž získávají přístup ke službám, jako je dělení sítě (network slicing), řízení politik přes [PCF](/mobilnisite/slovnik/pcf/) (Policy Control Function) a autentizace přes AUSF (Authentication Server Function). UE pracuje v režimu často označovaném jako „pouze LTE“, ale s jádrem 5G, což znamená, že používá rádiové protokoly E-UTRA, ale signalizace NAS probíhá s AMF 5GC. Tato konfigurace je základním kamenem nesamostatného (NSA) nasazení 5G, často používaným jako mezistupeň, kde LTE poskytuje širokoplošné pokrytí zakotvující vrstvu 5G NR pro kapacitu. Umožňuje operátorům využít své rozsáhlé investice do LTE a zároveň zavádět výhody jádra 5G, jako je dělení sítě pro různé typy služeb, integrace edge computingu a službami založená architektura (SBA) s modulárními síťovými funkcemi.

## K čemu slouží

E-UTRA/5GC bylo vytvořeno za účelem usnadnění plynulé a nákladově efektivní migrace ze sítí 4G na 5G. Primární problém, který řeší, je potřeba zavést pokročilé schopnosti 5G Core – jako je dělení sítě (network slicing), edge computing a službami založená architektura – bez nutnosti okamžité a kompletní výměny stávající rádiové přístupové sítě (RAN). Předtím bylo LTE výhradně spárováno s Evolved Packet Core (EPC), kterému chyběla flexibilita a cloud-nativní design potřebný pro různorodé požadavky služeb 5G (eMBB, URLLC, mMTC). Motivací bylo umožnit operátorům nasadit nové 5GC nezávisle na rozšiřování nového rádiového pokrytí 5G NR, což umožnilo časný start služeb 5G v oblastech s pokrytím LTE. Tento přístup snižuje počáteční kapitálové výdaje, urychluje uvedení služeb 5G na trh a poskytuje uživatelům bezproblémový zážitek během přechodu. Také umožňuje zavádění funkcí specifických pro 5G, jako je vylepšená QoS a řízení politik, pro uživatele LTE, čímž překlenuje mezeru mezi generacemi. Historicky toto oddělení představuje významný posun od těsné integrace viděné v předchozích generacích a nabízí větší flexibilitu nasazení.

## Klíčové vlastnosti

- Umožňuje LTE eNB (jako NG-eNB) připojit se přímo k 5G Core přes rozhraní NG
- Umožňuje LTE UE navazovat PDU relace a využívat služby 5G Core, jako je dělení sítě (network slicing)
- Podporuje nesamostatný (NSA) provoz s LTE zakotvujícím připojení 5G NR (EN-DC)
- Využívá službami založenou architekturu 5GC pro funkce řídicí roviny (AMF, SMF)
- Poskytuje migrační cestu k 5G s využitím stávajících investic do LTE infrastruktury
- Umožňuje pokročilé funkce 5G, jako je edge computing a řízení politik, pro uživatele LTE

## Související pojmy

- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)
- [EN-DC – E-UTRA NR Dual Connectivity with MCG using E-UTRA and SCG using NR](/mobilnisite/slovnik/en-dc/)

## Definující specifikace

- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [E-UTRA/5GC na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-utra-5gc/)
