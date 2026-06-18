---
slug: "swm"
url: "/mobilnisite/slovnik/swm/"
type: "slovnik"
title: "SWM – Software Management"
date: 2025-01-01
abbr: "SWM"
fullName: "Software Management"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/swm/"
summary: "Standardizovaný rámec pro správu softwaru v síťových prvcích, který umožňuje vzdálenou instalaci, aktivaci a deaktivaci. Je klíčový pro síťové operátory, aby mohli efektivně a spolehlivě nasazovat akt"
---

SWM je standardizovaný rámec pro správu softwaru v síťových prvcích, který umožňuje vzdálenou instalaci, aktivaci a deaktivaci aktualizací, záplat a nových funkcí.

## Popis

Software Management (SWM) je komplexní rámec definovaný 3GPP pro správu životního cyklu softwaru v telekomunikačních síťových prvcích. Funguje v širším kontextu Telecommunications Management Network ([TMN](/mobilnisite/slovnik/tmn/)) a 3GPP Management System a poskytuje standardizovaná rozhraní a procedury. Architektura je založena na modelu manažer-agent, kde centralizovaný Network Management System ([NMS](/mobilnisite/slovnik/nms/)) nebo Element Management System ([EMS](/mobilnisite/slovnik/ems/)) funguje jako manažer a spravované síťové prvky (NEs), jako jsou základnové stanice nebo uzly core sítě, hostují agenta. Komunikace typicky probíhá přes rozhraní jako Itf-N nebo pomocí protokolů jako [SNMP](/mobilnisite/slovnik/snmp/) či [CORBA](/mobilnisite/slovnik/corba/), jak je specifikováno v 3GPP Technical Specifications, přičemž primárním dokumentem podrobně popisujícím požadavky a informační model je 32.531.

Základní funkcionalita SWM zahrnuje několik klíčových operací. Distribuce softwaru zahrnuje zabezpečený a spolehlivý přenos softwarových balíčků (včetně spustitelného kódu, konfiguračních dat a metadat) z softwarového repozitáře na cílový [NE](/mobilnisite/slovnik/ne/). Po distribuci instalace softwaru připraví NE na hostování nové verze softwaru, často včetně kontrol integrity a alokace úložného prostoru. Kritickou fází je aktivace softwaru, kdy je nově nainstalovaný software převeden do spustitelného stavu, což může zahrnovat řízený přechod ze staré na novou verzi a případně vyžaduje restart NE nebo specifických procesů. SWM také spravuje deaktivaci softwaru, což umožňuje případný návrat k předchozí verzi, a odstranění softwaru za účelem smazání zastaralých balíčků z úložiště NE.

Role SWM je nedílnou součástí udržování síťové integrity, bezpečnosti a parity funkcí. Umožňuje koordinované hromadné nasazení a zajišťuje, že závislé síťové prvky jsou aktualizovány v určitém pořadí pro zachování interoperability. Rámec zahrnuje mechanismy pro kontrolu závislostí, správu verzí a komplexní auditní záznamy. Automatizací a standardizací těchto složitých procedur SWM snižuje provozní chyby, umožňuje rychlejší uvedení nových služeb na trh a představuje základní schopnost pro moderní, softwarově definované sítě, které vyžadují časté aktualizace a agilní provoz.

## K čemu slouží

SWM byl vytvořen, aby řešil provozní výzvy správy softwaru v stále složitějších a heterogenních 3GPP sítích. Před standardizací dodavatelé implementovali proprietární mechanismy aktualizace softwaru, což vedlo k vysokým integračním nákladům, provozní složitosti u více-dodavatelských sítí a zvýšenému riziku chyb při ručních aktualizačních postupech. Absence společného rámce ztěžovala rozsáhlá, koordinovaná nasazení softwaru a byla náchylná k chybám, což mohlo vést k výpadkům služeb nebo problémům s kompatibilitou mezi síťovými uzly.

Zavedení SWM v Release 8, jako součásti vylepšeného rámce Operation, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)), poskytlo jednotný, na dodavateli nezávislý přístup. Jeho vytvoření bylo motivováno potřebou provozní efektivity, snížení kapitálových a provozních výdajů ([CAPEX](/mobilnisite/slovnik/capex/)/OPEX) a zlepšení spolehlivosti sítě. Řeší problém nekonzistentních stavů softwaru v síti, což je klíčové pro aktivaci funkcí, aplikaci bezpečnostních záplat a oprav chyb. Definováním standardizovaného informačního modelu a procedur SWM umožňuje automatizaci, která je nezbytná pro správu obrovského počtu síťových prvků v moderních nasazeních 4G a 5G sítí, a tvoří tak páteř efektivní správy životního cyklu sítě.

## Klíčové vlastnosti

- Standardizované protokoly pro distribuci a přenos softwaru
- Řízené procedury aktivace a deaktivace softwaru s možností návratu
- Kontrola závislostí verzí softwaru a řešení konfliktů
- Komplexní auditní záznamy a správa inventáře softwarových balíčků
- Podpora plných i inkrementálních aktualizací softwaru
- Integrace se správou chyb a konfigurace pro koordinované operace

## Související pojmy

- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)
- [EMS – Enhanced Messaging Service](/mobilnisite/slovnik/ems/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)

## Definující specifikace

- **TS 32.531** (Rel-19) — 3GPP TS 32.531: SW Management Concepts & IRP Requirements

---

📖 **Anglický originál a plná specifikace:** [SWM na 3GPP Explorer](https://3gpp-explorer.com/glossary/swm/)
