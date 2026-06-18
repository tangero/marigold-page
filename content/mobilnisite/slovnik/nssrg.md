---
slug: "nssrg"
url: "/mobilnisite/slovnik/nssrg/"
type: "slovnik"
title: "NSSRG – Network Slice Simultaneous Registration Group"
date: 2026-01-01
abbr: "NSSRG"
fullName: "Network Slice Simultaneous Registration Group"
category: "Network Slicing"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nssrg/"
summary: "Skupina síťových řezů, pro kterou může být UE současně registrováno. Umožňuje jedinému zařízení udržovat aktivní registrace napříč více síťovými řezy a souběžně podporovat různé požadavky služeb bez n"
---

NSSRG je skupina síťových řezů, pro kterou může jediné UE udržovat současná aktivní registrace, což mu umožňuje souběžně podporovat různé požadavky služeb bez nutnosti nové registrace při přepínání služeb.

## Popis

Network Slice Simultaneous Registration Group (NSSRG, skupina pro současnou registraci síťových řezů) je koncept 3GPP, který definuje sadu jednoho nebo více instancí síťových řezů ([NSI](/mobilnisite/slovnik/nsi/)), pro které může uživatelské zařízení (UE) udržovat současné stavy registrace. Tento mechanismus je klíčový pro umožnění jedinému UE souběžně přistupovat ke službám z různých síťových řezů, z nichž každý může být přizpůsoben odlišným typům služeb, jako je rozšířené mobilní širokopásmové připojení (eMBB), ultra-spolehlivá komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) nebo hromadný IoT. NSSRG spravuje funkce pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) v 5G jádru sítě (5GC). Když UE zahájí registrační proceduru, může uvést požadované asistenční informace pro výběr síťového řezu ([NSSAI](/mobilnisite/slovnik/nssai/)). AMF ve spolupráci s funkcí pro výběr síťového řezu ([NSSF](/mobilnisite/slovnik/nssf/)) určí povolené NSSAI a na základě síťových politik a předplatitelských dat může přiřadit UE ke konkrétní NSSRG. AMF udržuje registrační kontext UE pro všechny řezy v rámci přiřazené NSSRG.

Z architektonického hlediska je koncept NSSRG úzce integrován s procedurami registrace a správy relací v 5G. UE registrované k NSSRG nemusí provádět novou registrační proceduru při zřizování relace protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)) na jiném síťovém řezu ve stejné skupině. Tím se snižuje signalizační režie a latence pro přístup ke službám. AMF uchovává společný registrační kontext pro UE napříč řezy ve skupině, zatímco jednotlivé funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) a funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)) jsou vybírány pro každou relaci PDU na základě konkrétního řezu. Identifikátor NSSRG je součástí kontextu UE v AMF a v jednotné správě dat (UDM).

Fungování závisí na schopnosti AMF podporovat více identifikátorů síťových řezů (S-NSSAI) v rámci jediného registračního kontextu. Během počáteční registrace nebo aktualizace registrace, pokud požadované S-NSSAI od UE patří podle konfigurace sítě do stejné NSSRG, může je AMF přijmout pod jedinou registrační oblastí a jedním globálně jedinečným dočasným identifikátorem 5G (5G-GUTI). Při mobilitě, pokud se UE přesune do oblasti, kde nejsou dostupné všechny řezy v jeho NSSRG, může AMF potřebovat upravit povolené NSSAI, ale registrace pro skupinu zůstává zachována pro dostupné řezy. To poskytuje rovnováhu mezi kontinuitou služeb a optimalizací síťových zdrojů. NSSRG je klíčovým prvkem pro efektivní provoz zařízení s více řezy, což je zásadní pro naplnění vize 5G o jediné fyzické síťové infrastruktuře podporující mnoho virtualizovaných sítí s různými charakteristikami.

## K čemu slouží

NSSRG bylo zavedeno, aby vyřešilo problém signalizační neefektivity a přerušení služeb, když UE potřebuje přistupovat k více síťovým řezům. Před jeho zavedením si UE typicky udržovalo stav registrace pro každý síťový řez. Přepínání mezi službami na různých řezech mohlo vyžadovat explicitní registrační procedury pro každý řez, což vedlo ke zvýšenému zatížení sítě signalizací a latenci pro uživatele. To bylo obzvláště problematické pro zařízení vyžadující současný přístup k řezům, jako je smartphone přehrávající vysoce propustný video stream (řez eMBB) a zároveň ovládající průmyslový senzor s nízkou latencí (řez URLLC).

Vytvoření NSSRG bylo motivováno potřebou škálovatelnějšího a efektivnějšího registračního modelu v řezané síti. Řeší omezení modelu jedna ku jedné mezi registrací UE a síťovým řezem, který se dobře neškáluje s rostoucím počtem řezů a UE. Seskupením řezů, které zařízení pravděpodobně použije společně, může síť udržovat jednotný stav správy mobility a připojení, což drasticky snižuje signalizaci řídicí roviny spojenou s registrací, deregistrací a periodickými aktualizacemi registrace. To je zásadní pro výkon sítě a životnost baterie zařízení.

Historicky se tento koncept vyvinul z modelu jedné registrace používaného v dřívějších mobilních generacích a z počáteční registrace v 5G s ohledem na řezy. NSSRG poskytuje střední cestu, nabízející výhody současného přístupu více registrací se signalizační efektivitou jedné registrace. Je to základní schopnost pro pokročilé případy užití, jako je síťové řezání pro podnikové služby, kde zařízení může potřebovat plynulý přístup jak k podnikovému řezu, tak k řezu veřejného internetu. Jeho zavedení ve vydání 17 odráží dospívání implementací síťového řezování směrem ke složitějším a realističtějším scénářům nasazení.

## Klíčové vlastnosti

- Umožňuje UE být současně registrováno k více instancím síťových řezů
- Snižuje signalizační režii odstraněním samostatných registračních procedur pro řezy ve skupině
- Spravováno AMF na základě předplatného UE, požadovaného NSSAI a síťových politik
- Podporuje efektivní mobilitu a kontinuitu služeb napříč více řezy
- Umožňuje nezávislé zřizování relací PDU na jakémkoli řezu ve skupině
- Integruje se s NSSF pro výběr řezu a s UDM pro předplatitelská data

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification

---

📖 **Anglický originál a plná specifikace:** [NSSRG na 3GPP Explorer](https://3gpp-explorer.com/glossary/nssrg/)
