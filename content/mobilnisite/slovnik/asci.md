---
slug: "asci"
url: "/mobilnisite/slovnik/asci/"
type: "slovnik"
title: "ASCI – Advanced Speech Call Items"
date: 2025-01-01
abbr: "ASCI"
fullName: "Advanced Speech Call Items"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/asci/"
summary: "ASCI je soubor funkcí 3GPP pro pokročilé skupinové a prioritní hlasové služby v sítích GSM/UMTS. Zahrnuje službu skupinového hovoru (VGCS), službu hlasového vysílání (VBS) a rozšířený systém víceúrovň"
---

ASCI je soubor funkcí 3GPP pro pokročilé skupinové a prioritní hlasové služby v sítích GSM/UMTS, zahrnující VGCS, VBS a eMLPP pro komunikaci s požadavky na vysokou dostupnost (mission-critical).

## Popis

Advanced Speech Call Items (ASCI) je komplexní rámec definovaný ve specifikacích 3GPP, který zavádí tři specializované hlasové komunikační služby do sítí GSM a UMTS: Voice Group Call Service (VGCS), Voice Broadcast Service (VBS) a enhanced Multi-Level Precedence and Preemption (eMLPP). Tyto služby byly navrženy tak, aby rozšířily tradiční možnosti okruhově přepínaného hlasu a podporovaly profesionální a kritické komunikační požadavky, které byly dříve dostupné pouze ve specializovaných trunkových radiových systémech, jako jsou TETRA nebo P25.

VGCS umožňuje poloduplexní skupinové volání, kdy jeden uživatel hovoří a více uživatelů naslouchá, podobně jako u systému vysílačky, ale s využitím infrastruktury mobilní sítě. Služba vytváří oblast skupinového hovoru na základě konfigurace buněk a uživatelé v této oblasti se mohou k hovoru připojit automaticky nebo manuálně. Síť spravuje soutěž o uplink, kdy se více uživatelů může pokusit hovořit, a uděluje právo mluvit vždy pouze jednomu mluvčímu. VBS poskytuje jednosměrnou vysílací službu, kdy autorizovaný uživatel přenáší hlas všem posluchačům v definované vysílací oblasti, bez možnosti uplink pro posluchače. To je zvláště užitečné pro oznámení, výstrahy při mimořádných událostech nebo dispečerské pokyny.

Enhanced Multi-Level Precedence and Preemption (eMLPP) zavádí prioritní mechanismy pro hlasové hovory, umožňující vysokoprioritním hovorům vytěsnit hovory s nižší prioritou při přetížení síťových zdrojů. Systém definuje více úrovní priority (obvykle 1–7, přičemž 1 je nejvyšší) a zahrnuje jak schopnosti přednosti (priorita ve frontě), tak vytěsnění (převzetí zdrojů). Architektura zahrnuje úpravy napříč více síťovými prvky: Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) zpracovává rozhodnutí o prioritizaci a vytěsnění hovorů, Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)) nebo Radio Network Controller (RNC) spravuje přidělování rádiových zdrojů na základě priority a Mobile Station ([MS](/mobilnisite/slovnik/ms/)) musí podporovat indikátory priority a oznámení o vytěsnění.

Služby ASCI vyžadují specifickou síťovou konfiguraci včetně definic oblastí pro skupinové/vysílací hovory, profilů účastníků s autorizací služby a přiřazení úrovní priority. Implementace zahrnuje vylepšení signalizace na rozhraní Um/Uu, rozhraní A mezi BSC a MSC a rozhraních jádra sítě. Pro VGCS a VBS síť vytváří společný provozní kanál v buňkách patřících do servisní oblasti, což umožňuje efektivnější využití rádiových zdrojů ve srovnání s vytvářením individuálních hovorů ke každému účastníkovi. eMLPP se integruje s existujícími procedurami sestavování hovoru a předávání služby, přidává informační prvky priority do signalizačních zpráv a implementuje algoritmy správy zdrojů, které berou v úvahu úrovně priority během scénářů přetížení.

## K čemu slouží

ASCI bylo vytvořeno, aby uspokojilo rostoucí poptávku po schopnostech profesionální mobilní radiokomunikace (PMR) v rámci veřejných mobilních sítí. Před ASCI musely organizace vyžadující skupinovou komunikaci, vysílání oznámení nebo prioritní volání nasazovat a udržovat samostatné vyhrazené sítě, jako je TETRA, což zahrnovalo významné náklady na infrastrukturu a omezené pokrytí. Integrací těchto funkcí do sítí GSM/UMTS umožnilo ASCI nákladově efektivní alternativu s širším pokrytím, která využívá stávající infrastrukturu mobilních sítí a zároveň poskytuje podobnou funkcionalitu jako tradiční systémy PMR.

Hlavní motivace vycházela z organizací veřejné bezpečnosti, dopravních společností a průmyslových podniků, které potřebovaly spolehlivou skupinovou komunikaci a prioritní mechanismy pro kritické operace. Tradiční hlasové služby mobilních sítí podporovaly pouze bodové hovory bez správy skupin nebo prioritních funkcí, což je činilo nevhodnými pro dispečerské operace, koordinaci zásahů při mimořádných událostech nebo komunikaci průmyslových týmů. ASCI tyto omezení řešilo zavedením standardizovaných mechanismů pro sestavení skupinového hovoru, distribuci vysílání a prioritizaci hovorů v rámci rámce 3GPP.

Dalším klíčovým problémem, který ASCI řešilo, byla efektivita využití spektra pro skupinovou komunikaci. Namísto vytváření individuálních okruhově přepínaných spojení ke každému členovi skupiny (což by spotřebovávalo nadměrné síťové zdroje) využívají VGCS a VBS sdílené rádiové zdroje v rámci definované geografické oblasti. Toto efektivní využití zdrojů v kombinaci s rozsáhlým pokrytím mobilních sítí učinilo ASCI zvláště atraktivním pro aplikace, jako je železniční komunikace, kde vlaky pohybující se po velkých územích potřebují nepřetržité schopnosti skupinové komunikace bez častého překonfigurování.

## Klíčové vlastnosti

- Poloduplexní skupinové volání s dynamickou správou práva mluvit (VGCS)
- Jednosměrná vysílací služba pro oznámení a výstrahy (VBS)
- Víceúrovňová priorita se schopnostmi vytěsnění (eMLPP)
- Geografická konfigurace servisní oblasti pro skupinové/vysílací hovory
- Efektivní využití rádiových zdrojů prostřednictvím sdílených kanálů
- Integrace s existujícími systémy autentizace a účtování GSM/UMTS

## Související pojmy

- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.053** (Rel-19) — Tandem Free Operation (TFO) Stage 1
- **TS 27.007** (Rel-19) — AT Command Set for UE

---

📖 **Anglický originál a plná specifikace:** [ASCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/asci/)
