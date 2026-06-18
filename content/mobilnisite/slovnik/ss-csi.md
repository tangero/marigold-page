---
slug: "ss-csi"
url: "/mobilnisite/slovnik/ss-csi/"
type: "slovnik"
title: "SS-CSI – Supplementary Service Notification CAMEL Subscription Information"
date: 2025-01-01
abbr: "SS-CSI"
fullName: "Supplementary Service Notification CAMEL Subscription Information"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ss-csi/"
summary: "SS-CSI je parametr předplatného CAMEL uložený v HLR, který spouští provádění služby CAMEL při výskytu události související s doplňkovou službou u mobilního účastníka. Umožňuje domácí síti uplatnit vla"
---

SS-CSI je parametr předplatného CAMEL uložený v HLR, který spouští službu CAMEL při události doplňkové služby, což umožňuje uplatnit vlastní logiku, například účtování za služby jako přesměrování hovoru.

## Popis

Supplementary Service Notification [CAMEL](/mobilnisite/slovnik/camel/) Subscription Information (SS-CSI) je specifický typ předplatných dat CAMEL (Customised Applications for Mobile networks Enhanced Logic). CAMEL je standard 3GPP pro služby inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) v mobilních sítích, který umožňuje operátorovi domácí sítě definovat a řídit přidané služby pro své účastníky i při roamingu. SS-CSI je spouštěcí mechanismus, který spojuje výskyt události doplňkové služby ([SS](/mobilnisite/slovnik/ss/)) s vyvoláním servisní logiky CAMEL, která je provedena na vyhrazeném uzlu nazývaném CAMEL Service Environment ([CSE](/mobilnisite/slovnik/cse/)) nebo Service Control Point ([SCP](/mobilnisite/slovnik/scp/)).

Architektonicky je SS-CSI jednou z několika sad dat [CSI](/mobilnisite/slovnik/csi/) (CAMEL Subscription Information) uložených v profilu účastníka v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)). Když je profil účastníka stažen do Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)) nebo Serving GPRS Support Node (SGSN) během registrace, je SS-CSI součástí přenosu. Klíčové funkční entity zapojené do procesu jsou HLR (úložiště dat), MSC nebo GMSC (Service Switching Function – SSF, která detekuje spouštěcí podmínku) a gsmSCF (GSM Service Control Function, tj. SCP, který provádí vlastní servisní logiku). Rozhraním mezi SSF a gsmSCF je protokol CAP (CAMEL Application Part).

Mechanismus funguje následovně: Když mobilní účastník provede operaci související s doplňkovou službou – například aktivuje přesměrování hovoru bez podmínek (CFU), deaktivuje blokování hovorů nebo obdrží notifikaci o vyvolání čekání hovoru – MSC (v roli SSF) zkontroluje v profilu účastníka přítomnost SS-CSI. Pokud je SS-CSI přítomno a konkrétní událost SS odpovídá spouštěcím kritériím v něm definovaným, MSC pozastaví běžné zpracování SS a odešle zprávu CAP (např. InitialDP) na gsmSCF uvedené v datech SS-CSI. Tato zpráva obsahuje podrobnosti o události SS, jako je typ doplňkové služby (např. CFU), identitu účastníka a jakékoli relevantní parametry (jako číslo, na které se hovor přesměrovává).

Po přijetí spuštění gsmSCF provede svou vlastní servisní logiku. Tato logika může provádět různé akce. Běžným případem užití je speciální účtování: domácí síť může chtít uplatnit jiný tarif, když účastník aktivuje přesměrování hovoru na mezinárodní číslo. gsmSCF může pomocí zpráv CAP instruovat MSC, aby uplatnil specifickou sazbu účtování. Dalším případem užití je notifikace: domácí síť může chtít poslat SMS notifikaci účastníkovi nebo do manažerského systému pokaždé, když je změněna hodnotná SS jako blokování hovorů, a to pro účely bezpečnostního auditu. Po provedení logiky CAMEL gsmSCF událost zpracuje. Poté může instruovat MSC (pomocí operace CAP Continue nebo jiných), aby pokračovalo v běžném zpracování SS, nebo může uplatnit vlastní logiku. Například gsmSCF může vygenerovat záznam o účtování za aktivaci SS, poslat účastníkovi SMS notifikaci potvrzující změnu nebo dokonce upravit parametry operace SS na základě obchodních pravidel (např. povolit přesměrování hovoru pouze na konkrétní čísla). Po přijetí instrukcí MSC obnoví a dokončí proceduru doplňkové služby.

## K čemu slouží

SS-CSI bylo vytvořeno za účelem rozšíření možností a flexibility platformy inteligentní sítě CAMEL na události související s doplňkovými službami. Před zavedením CAMEL bylo řízení a účtování doplňkových služeb převážně statické a zabudované do ústředen jádrové sítě (MSC). Operátoři neměli možnost snadno zavádět vlastní, interaktivní reakce v reálném čase na základě využití SS. SS-CSI tento problém řeší tím, že poskytuje standardizovaný spouštěcí bod, který umožňuje vyvolání servisní logiky domácí sítě (na SCP) právě ve chvíli, kdy účastník interaguje s doplňkovou službou.

Hlavními motivy byly vylepšená kontrola služeb, sofistikované modely účtování a lepší interakce se zákazníkem. Pro kontrolu služeb mohl operátor použít SS-CSI k implementaci obchodních pravidel, jako je zabránění přesměrování hovoru na mezinárodní čísla pro předplacené účastníky nebo vyžadování PINu pro aktivaci určitých blokovacích služeb. Pro účtování umožnilo detailní, událostmi řízené fakturace za využití SS. Například operátor mohl účtovat malý poplatek pokaždé, když účastník aktivoval přesměrování hovoru nebo použil konferenční hovor, což by bylo obtížné pouze s tradičním účtováním založeným na záznamech o hovorech (CDR).

Navíc SS-CSI umožnilo proaktivní péči o zákazníky a notifikační služby. Když účastník přerušil do zahraniční sítě a aktivoval přesměrování hovoru, SCP domácí sítě mohl být prostřednictvím SS-CSI notifikován a okamžitě poslat účastníkovi na telefon SMS potvrzení o aktivaci a případně informaci o případných souvisejících poplatcích. Toto zlepšilo transparentnost a uživatelský zážitek, zejména v roamingu, kde účastníci mohli být nejistí ohledně dostupnosti služeb a nákladů. V podstatě SS-CSI překlenulo propast mezi standardizovaným světem doplňkových služeb založeným na ústřednách a flexibilním, programovatelným světem služeb inteligentní sítě, což operátorům umožnilo diferencovat svou nabídku a spravovat služby podrobněji.

## Klíčové vlastnosti

- Parametr předplatného CAMEL uložený v HLR/VLR, který spojuje události doplňkových služeb s logikou inteligentní sítě
- Vyvolá gsmSCF (Service Control Point) domácí sítě, když účastník aktivuje, deaktivuje nebo vyvolá doplňkovou službu
- Pro komunikaci mezi MSC (SSF) a gsmSCF používá protokol CAP (CAMEL Application Part)
- Umožňuje vlastní politiky účtování, notifikací nebo řízení pro využití doplňkových služeb
- Funguje transparentně pro účastníka a nemění standardizované chování SS, pokud není instruováno gsmSCF
- Zvláště cenné pro správu a monetizaci využití SS v roamingu

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TR 21.978** (Rel-4) — CAMEL Control of VoIP Services Feasibility Study
- **TS 23.031** (Rel-19) — Fraud Information Gathering System (FIGS) - Stage 2

---

📖 **Anglický originál a plná specifikace:** [SS-CSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ss-csi/)
