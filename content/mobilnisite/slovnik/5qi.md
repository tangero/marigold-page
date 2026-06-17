---
slug: "5qi"
url: "/mobilnisite/slovnik/5qi/"
type: "slovnik"
title: "5QI – 5G QoS Identifier"
date: 2026-01-01
abbr: "5QI"
fullName: "5G QoS Identifier"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/5qi/"
summary: "5QI je standardizovaný skalární identifikátor, který se mapuje na konkrétní charakteristiky QoS v 5G sítích. Definuje rozpočet zpoždění paketů (PDB), míru chybovosti paketů (PER), úroveň priority a vý"
---

5QI je standardizovaný skalární identifikátor, který se mapuje na konkrétní charakteristiky kvality služby (QoS) v 5G, jako je rozpočet zpoždění paketů a míra chyb, aby umožnil konzistentní zpracování kvality služby v celé síti.

## Popis

Identifikátor kvality služby pro 5G (5QI) je základním mechanismem v architektuře 5G systému (5GS) pro správu kvality služby (QoS). Je to skalární hodnota v rozsahu od 1 do 255, kde standardizované hodnoty (1-89) mají předdefinované charakteristiky QoS stanovené ve specifikacích 3GPP, zatímco dynamické hodnoty (90-254) lze přiřadit s parametry QoS specifickými pro operátora. Každá hodnota 5QI se mapuje na konkrétní profil QoS obsahující pět klíčových parametrů: typ prostředku ([GBR](/mobilnisite/slovnik/gbr/), Delay Critical GBR nebo Non-GBR), úroveň priority, rozpočet zpoždění paketů (PDB), míra chybovosti paketů (PER) a průměrovací okno (pouze pro toky GBR).

Když je zřízena relace protokolové datové jednotky (PDU), jádro 5G sítě (5GC) přiřadí jeden nebo více toků QoS identifikovaných svými hodnotami 5QI. Funkce pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) tyto požadavky QoS komunikuje k rádiové přístupové síti (RAN) přes rozhraní [N2](/mobilnisite/slovnik/n2/). RAN poté mapuje každý tok QoS na příslušné datové rádiové přenosy ([DRB](/mobilnisite/slovnik/drb/)) pomocí pravidel mapování toku QoS na DRB. Tento hierarchický přístup odděluje řízení QoS (v 5GC) od správy přenosů (v RAN), což poskytuje flexibilitu a škálovatelnost.

Mechanismus 5QI funguje prostřednictvím standardizovaných signalizačních procedur. Během zřizování nebo modifikace PDU relace funkce pro správu relací ([SMF](/mobilnisite/slovnik/smf/)) určí příslušný 5QI na základě požadavků služby a profilu účastníka. SMF tuto informaci odešle funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) pro označování paketů a do RAN přes AMF. V uživatelské rovině jsou pakety označeny identifikátory toků QoS (QFI) odvozenými od hodnot 5QI, což umožňuje konzistentní zacházení s QoS napříč síťovými uzly. RAN používá tato označení k aplikaci příslušného plánování, řízení přístupu a konfigurací spojové vrstvy.

Klíčové architektonické komponenty zapojené do implementace 5QI zahrnují funkci řízení politik ([PCF](/mobilnisite/slovnik/pcf/)), která poskytuje pravidla politik obsahující přiřazení 5QI; SMF, která tato pravidla vynucuje; UPF, která provádí označování paketů a řízení přenosové rychlosti; a gNB, které implementuje plánování rádiových prostředků na základě parametrů 5QI. Systém podporuje jak reflexivní QoS, kde uživatelské zařízení (UE) může odvodit pravidla QoS z provozu v downlinku, tak explicitní signalizaci QoS prostřednictvím protokolů [NAS](/mobilnisite/slovnik/nas/) a RRC.

5QI hraje klíčovou roli při umožnění síťového segmentování (network slicing) a diferenciace služeb. Různé síťové segmenty mohou používat různé hodnoty 5QI k dosažení svých specifických požadavků na výkon. Standardizované hodnoty 5QI pokrývají široké spektrum služeb včetně konverzačního hlasu, živého streamování, autonomního řízení, průmyslové automatizace a aplikací masivního internetu věcí (IoT). Tento standardizovaný přístup zajišťuje interoperabilitu mezi zařízeními různých výrobců a konzistentní uživatelský zážitek z QoS.

## K čemu slouží

5QI byl vytvořen, aby řešil omezení předchozích mechanismů QoS v sítích 4G/LTE, konkrétně QCI (QoS Class Identifier). Zatímco QCI dobře sloužilo pro služby 4G, postrádalo granularitu a flexibilitu potřebnou pro různorodé případy užití v 5G, včetně ultra-spolehlivé komunikace s nízkou latencí (URLLC), rozšířeného mobilního širokopásmového přístupu (eMBB) a masivní komunikace mezi stroji (mMTC). Model QoS založený na přenosech v systému 4G byl pro architekturu založenou na službách a požadavky na síťové segmentování v 5G příliš rigidní.

5QI řeší několik klíčových problémů: Za prvé poskytuje jemnější granularitu pro služby kritické na zpoždění s konkrétními hodnotami pro průmyslovou automatizaci, inteligentní dopravní systémy a aplikace dálkového ovládání. Za druhé zavádí typ prostředku Delay Critical GBR speciálně pro služby URLLC vyžadující jak garantovanou přenosovou rychlost, tak přísné limity latence. Za třetí, 5QI umožňuje efektivnější využití prostředků díky vylepšenému zpracování priorit a oddělení řízení QoS od správy přenosů.

Historický kontext vývoje 5QI zahrnuje potřebu podpořit požadavky vertikálních průmyslů identifikované ve studijních položkách 3GPP, jako jsou TR 22.891 a TR 22.804. Tyto studie odhalily, že předchozí mechanismy QoS nedokázaly adekvátně podporovat služby s protichůdnými požadavky fungující současně na stejném zařízení, jako je rozšířená realita (vyžadující vysokou šířku pásma) a komunikace vozidlo-se-vším (vyžadující ultra-nízkou latenci). 5QI poskytuje základ pro splnění těchto různorodých požadavků prostřednictvím standardizovaných, ale flexibilních profilů QoS.

## Klíčové vlastnosti

- Skalární identifikátor mapovaný na předdefinované charakteristiky QoS
- Podporuje tři typy prostředků: GBR, Delay Critical GBR a Non-GBR
- Definuje rozpočet zpoždění paketů (PDB) od 10 ms do 3000 ms
- Specifikuje míru chybovosti paketů (PER) od 10^-2 do 10^-6
- Zahrnuje úrovně priority od 1 (nejvyšší) do 127 (nejnižší)
- Umožňuje flexibilitu mapování toku QoS na DRB v RAN

## Definující specifikace

- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TR 22.832** (Rel-17) — Study on cyber-physical control in vertical domains
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.764** (Rel-17) — Study on V2X Application Layer Enhancements
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 26.502** (Rel-19) — 5G Multicast-Broadcast User Services Architecture
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TS 28.802** (Rel-15) — Management Study for 5G Network Architecture
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [5QI na 3GPP Explorer](https://3gpp-explorer.com/glossary/5qi/)
