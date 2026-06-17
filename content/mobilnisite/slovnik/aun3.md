---
slug: "aun3"
url: "/mobilnisite/slovnik/aun3/"
type: "slovnik"
title: "AUN3 – Authenticable Non-3GPP Devices"
date: 2026-01-01
abbr: "AUN3"
fullName: "Authenticable Non-3GPP Devices"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/aun3/"
summary: "AUN3 označuje ne-3GPP zařízení (jako Wi-Fi přístupové body nebo zařízení pevných sítí), která může jádro 5G sítě (5G core) ověřit. Umožňuje bezpečnou integraci různorodých přístupových technologií do"
---

AUN3 je termín pro ověřitelná ne-3GPP zařízení (authenticable non-3GPP devices), například Wi-Fi přístupové body, která může jádro 5G sítě (5G core) ověřit, aby bezpečně integrovala různorodé přístupové technologie a rozšířila služby.

## Popis

Ověřitelná ne-3GPP zařízení (Authenticable Non-3GPP, AUN3) představují klíčovou součást konvergované síťové architektury 5G, která umožňuje bezpečnou integraci ne-3GPP přístupových sítí s jádrem 5G (5G Core, 5GC). Tato zařízení zahrnují Wi-Fi přístupové body, brány pevných sítí a další přístupové vybavení, které může navázat důvěryhodná spojení k systému 5G prostřednictvím standardizovaných ověřovacích procedur. Rámec AUN3 umožňuje, aby byly tyto heterogenní přístupové technologie považovány za důvěryhodné vstupní body do sítě 5G, podléhající stejným bezpečnostním kontrolám a politikám jako nativní 3GPP rádiový přístup.

Technická implementace AUN3 zahrnuje několik klíčových komponent pracujících ve vzájemné koordinaci. Funkce pro propojení s ne-3GPP sítěmi (Non-3GPP Interworking Function, [N3IWF](/mobilnisite/slovnik/n3iwf/)) slouží jako primární rozhraní mezi ne-3GPP přístupovými sítěmi a jádrem 5G Core a navazuje [IPsec](/mobilnisite/slovnik/ipsec/) tunely pro bezpečný přenos dat. Funkce autentizačního serveru (Authentication Server Function, [AUSF](/mobilnisite/slovnik/ausf/)) provádí vlastní ověření zařízení pomocí metod rozšiřitelného autentizačního protokolu (Extensible Authentication Protocol, [EAP](/mobilnisite/slovnik/eap/)), zatímco jednotná správa dat (Unified Data Management, [UDM](/mobilnisite/slovnik/udm/)) ukládá přihlašovací údaje a údaje o předplatném. Funkce správy přístupu a mobility (Access and Mobility Management Function, [AMF](/mobilnisite/slovnik/amf/)) koordinuje celkové ověřovací a registrační procedury, zajišťující plynulou mobilitu mezi 3GPP a ne-3GPP přístupem.

Ověřovací proces pro AUN3 zařízení sleduje sofistikovaný tok protokolu definovaný ve specifikacích 3GPP. Když se zařízení pokusí připojit prostřednictvím ne-3GPP přístupu, zahájí ověřovací požadavek, který prochází přes N3IWF k AMF. AMF následně koordinuje s AUSF provedení ověření založeného na EAP, což může zahrnovat různé metody včetně EAP-AKA' pro 5G-specifickou autentizaci nebo EAP-TLS pro autentizaci založenou na certifikátech. Během tohoto procesu zařízení prokazuje svou identitu pomocí přihlašovacích údajů uložených v univerzálním SIM modulu (USIM) nebo prostřednictvím mechanismů založených na certifikátech, zatímco síť se sama ověří vůči zařízení, aby se zabránilo útoku typu man-in-the-middle.

Bezpečnostní aspekty pro AUN3 zařízení jsou komplexní a vícevrstvé. Rámec vyžaduje vzájemné ověření mezi zařízením a sítí, což zajišťuje, že obě strany ověří své identity. Bezpečnostní asociace IPsec poskytují ochranu důvěrnosti a integrity pro provoz v uživatelské rovině, zatímco signalizace v řídicí rovině je chráněna mechanismy [NAS](/mobilnisite/slovnik/nas/) zabezpečení. Systém také podporuje správu hierarchie klíčů, s odvozenými samostatnými klíči pro různé bezpečnostní kontexty včetně ochrany integrity, důvěrnosti a procedur obnovy klíčů. Tento vrstvený bezpečnostní přístup zajišťuje, že i když se fyzický přístupový médium liší od 3GPP rádiového přístupu, úroveň zabezpečení zůstává ekvivalentní.

Role AUN3 v ekosystému 5G přesahuje základní konektivitu a umožňuje pokročilé služební schopnosti. Ověřováním ne-3GPP zařízení mohou operátoři nabízet plynulou kontinuitu služeb při pohybu uživatelů mezi mobilními a Wi-Fi sítěmi, implementovat konzistentní politiky kvality služeb napříč různými typy přístupu a umožnit síťové segmentování (network slicing), které zahrnuje jak 3GPP, tak ne-3GPP domény. Tato konvergenční schopnost je obzvláště důležitá pro podniková nasazení, kde soukromé 5G sítě často integrují s existující Wi-Fi infrastrukturou, a pro scénáře pevného bezdrátového přístupu (fixed wireless access), kde jsou služby jádra 5G poskytovány prostřednictvím nemobilních technologií poslední míle.

## K čemu slouží

Rámec AUN3 byl vyvinut, aby řešil rostoucí potřebu konvergovaných síťových architektur, které mohou plynule integrovat různorodé přístupové technologie pod jednotnou bezpečnostní a správní strukturu. Jak se sítě 5G vyvíjely mimo tradiční mobilní nasazení, operátoři čelili rostoucímu tlaku na začlenění Wi-Fi, pevného přístupu a dalších ne-3GPP technologií do své nabídky služeb při zachování robustních bezpečnostních standardů očekávaných od systémů 3GPP. Předchozí přístupy k integraci ne-3GPP, jako ty v 4G EPC, nabízely omezené možnosti ověřování a často zacházely s ne-3GPP přístupem jako s druhotnými nebo méně bezpečnými alternativami.

Historicky integrace ne-3GPP přístupu trpěla fragmentovanými implementacemi zabezpečení a nekonzistentními ověřovacími mechanismy napříč různými technologiemi. Wi-Fi sítě typicky používaly WPA2/WPA3 s oddělenými autentizačními servery, zatímco pevné sítě používaly různé proprietární autentizační metody. Tato fragmentace vytvářela bezpečnostní mezery, komplikovala scénáře roamingu a bránila operátorům v uplatňování konzistentních kontrolních politik v celé jejich síťové stopě. Rámec AUN3 řeší tato omezení tím, že poskytuje standardizovaný, na 3GPP zarovnaný ověřovací rámec, který podřazuje ne-3GPP zařízení pod stejnou bezpečnostní správu jako nativní přístup 5G.

Vytvoření AUN3 bylo motivováno několika klíčovými průmyslovými trendy: rozšířením technologií Wi-Fi 6/6E nabízejících výkon srovnatelný s 5G NR, vznikem pevného bezdrátového přístupu (fixed wireless access) jako primární metody doručování širokopásmových služeb a rostoucí poptávkou podniků po privátních sítích, které kombinují mobilní a nemobilní technologie. Tím, že rámec umožňuje bezpečné ověření ne-3GPP zařízení, podporuje tyto případy užití při zachování principů end-to-end zabezpečení, které jsou zásadní pro systémy 3GPP. To operátorům umožňuje využít jejich stávající investice do infrastruktury a zároveň rozšířit pokrytí a schopnosti služeb prostřednictvím heterogenní přístupové integrace.

## Klíčové vlastnosti

- Standardizované ověřování ne-3GPP zařízení pomocí bezpečnostních protokolů 3GPP
- Podpora autentizačních metod EAP-AKA' a EAP-TLS
- Integrace s autentizačními funkcemi jádra 5G (AUSF, UDM)
- Zabezpečení založené na IPsec pro ochranu uživatelské roviny
- Plynulá mobilita mezi 3GPP a ne-3GPP přístupem
- Konzistentní bezpečnostní politiky napříč heterogenními sítěmi

## Související pojmy

- [N3IWF – Non-3GPP access InterWorking Function](/mobilnisite/slovnik/n3iwf/)
- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 29.413** (Rel-19) — NGAP for Non-3GPP Access
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)

---

📖 **Anglický originál a plná specifikace:** [AUN3 na 3GPP Explorer](https://3gpp-explorer.com/glossary/aun3/)
