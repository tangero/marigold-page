---
slug: "ucmf"
url: "/mobilnisite/slovnik/ucmf/"
type: "slovnik"
title: "UCMF – UE radio Capability Management Function"
date: 2026-01-01
abbr: "UCMF"
fullName: "UE radio Capability Management Function"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ucmf/"
summary: "Funkce jádra sítě zavedená v 5G pro centrální ukládání, správu a poskytování rádiových schopností UE. Odstraňuje potřebu redundantní signalizace tím, že umožňuje síti dotazovat se na centrální úložišt"
---

UCMF je funkce jádra sítě, která centrálně ukládá, spravuje a poskytuje rádiové schopnosti UE, čímž odstraňuje redundantní signalizaci a zvyšuje efektivitu.

## Popis

Funkce správy rádiových schopností UE (UCMF) je klíčovou součástí architektury sítě 5G Core (5GC), konkrétně navrženou pro správu informací o rádiových schopnostech UE. Funguje jako centralizované úložiště a zpracovatelský prvek pro Radio Capability ID (RCID) a přidružené informace o rádiových schopnostech UE. Primární architektonická role UCMF spočívá v interakci s jinými síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)), jako je Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)), prostřednictvím rozhraní založených na službách, primárně Nucmf. Když se UE připojí k síti, AMF nemusí mít úplné podrobnosti o rádiových schopnostech UE. Místo toho může mít pouze UE Radio Capability ID. AMF pak může vyvolat servisní operaci Nucmf_Get na UCMF a poskytnout toto RCID. UCMF odpoví kompletními informacemi o rádiových schopnostech UE odpovídajícími tomuto ID, které může AMF následně předat přístupové rádiové síti (RAN) pro optimální konfiguraci rádiových prostředků.

Fungování UCMF zahrnuje proces správy životního cyklu dat o schopnostech. Může přijímat informace o rádiových schopnostech UE od AMF (např. když se připojí nový typ UE) a generovat pro ně nové, jedinečné RCID. Toto RCID je kompaktní identifikátor, který může být uložen v univerzálním [SIM](/mobilnisite/slovnik/sim/) modulu ([USIM](/mobilnisite/slovnik/usim/)) UE nebo ve funkci Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) 5GC, přidružený k profilu účastníka. Při následných připojeních k síti může UE nebo UDM poskytnout toto RCID, což umožní síti načíst plné schopnosti z UCMF, aniž by UE muselo opakovaně přenášet velký datový blok schopností vzduchem. Tento mechanismus je klíčový pro zařízení s omezenou šířkou pásma a pro snížení signalizační režie.

Role UCMF přesahuje pouhé ukládání; zajišťuje konzistenci a platnost dat o schopnostech v celé síti. Může validovat příchozí informace o schopnostech, spravovat verzování a zajišťovat mapování mezi různými RCID a jejich odpovídajícími datovými sadami. Oddělením objemných informací o rádiových schopnostech od rutinních signalizačních procedur umožňuje UCMF efektivnější správu mobility, rychlejší navázání spojení a škálovatelnou podporu scénářů hromadné komunikace mezi stroji (mMTC), kde se k síti připojuje obrovské množství různorodých IoT zařízení se specifickými rádiovými profily. Její návrh je základním kamenem architektury založené na službách 5GC, podporujícím znovupoužitelnost síťových funkcí a zefektivnění provozu.

## K čemu slouží

UCMF byla vytvořena, aby vyřešila významné neefektivity v zacházení s rádiovými schopnostmi UE v předchozích generacích, jako je 4G LTE. V legacy systémech muselo UE často přenášet svůj kompletní soubor rádiových schopností – což mohl být velký datový blok – během počátečního připojení nebo procedur předávání. Tento proces spotřebovával cenné rádiové prostředky, zvyšoval signalizační latenci a vyčerpával životnost baterie zařízení, což byly problémy umocněné rostoucí diverzitou a množstvím IoT zařízení se specializovanými schopnostmi.

Motivace pro UCMF ve 3GPP Release 16 přímo souvisela s 5G designovými principy efektivity a škálovatelnosti pro heterogenní zařízení. Předchozí přístup se neškáloval dobře pro hromadná IoT nasazení a zařízení s omezenými prostředky. Zavedením centralizované správní funkce může síť přiřadit sadě schopností UE lehký Radio Capability ID (RCID). Toto ID, namísto plných dat, je používáno ve většině signalizace, což drasticky snižuje režii. Také umožňuje aktualizace a správu informací o schopnostech na straně sítě, což je nezbytné pro zavádění podpory nových rádiových funkcí nebo pro zařízení, jejichž schopnosti mohou být aktualizovány vzdáleně.

Dále UCMF řeší problém 'signalizačních bouří' způsobených schopnostmi, které by mohly nastat během obnovy sítě nebo hromadného probouzení zařízení. Poskytuje deterministickou a efektivní metodu pro RAN, jak získat potřebná konfigurační data, což umožňuje optimalizovaný rádiový výkon a přidělování prostředků od samého začátku spojení. Její vytvoření bylo strategickým vylepšením architektury 5GC, v souladu s cíli automatizace sítě, snížení provozní složitosti a lepší podpory trojúhelníku 5G případů užití: vylepšeného mobilního širokopásmového připojení (eMBB), ultra-spolehlivé komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a hromadné komunikace mezi stroji (mMTC).

## Klíčové vlastnosti

- Centralizované úložiště pro informace o rádiových schopnostech UE a mapování Radio Capability ID (RCID)
- Rozhraní založené na službách (Nucmf) pro interakci s AMF a dalšími autorizovanými NF
- Generování, přiřazování a správa životního cyklu jedinečných RCID
- Validace a ukládání informací o rádiových schopnostech UE poskytnutých sítí
- Efektivní načítání plných rádiových schopností pouze pomocí kompaktního RCID
- Snížení režie signalizace vzduchem pro přenos schopností UE

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.673** (Rel-19) — Nucmf Service Based Interface Stage 3
- **TS 29.674** (Rel-19) — UE Radio Capability Management Protocol (URCMP)
- **TS 29.675** (Rel-19) — UE Radio Capability Provisioning Service

---

📖 **Anglický originál a plná specifikace:** [UCMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ucmf/)
