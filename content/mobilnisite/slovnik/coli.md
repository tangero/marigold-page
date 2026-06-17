---
slug: "coli"
url: "/mobilnisite/slovnik/coli/"
type: "slovnik"
title: "COLI – Connected Line Identity"
date: 2025-01-01
abbr: "COLI"
fullName: "Connected Line Identity"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/coli/"
summary: "COLI (Connected Line Identity) je doplňková služba, která poskytuje identitu účastníka, ke kterému je hovor skutečně spojen, což se může lišit od původně vytočeného čísla. Je klíčová pro přesné účtová"
---

COLI je doplňková služba, která poskytuje identitu účastníka, ke kterému je hovor skutečně spojen, což se může lišit od původně vytočeného čísla.

## Popis

COLI (Connected Line Identity) je doplňková služba definovaná ve specifikacích 3GPP, která funguje v okruhově přepínané ([CS](/mobilnisite/slovnik/cs/)) telefonní doméně. Jejím hlavním účelem je identifikovat a poskytnout síti skutečné telefonní číslo (nebo identitu) účastníka, který hovor přijal, tedy tzv. 'spojenou linku'. To se liší od původně vytočeného čísla (volané linky), zejména ve scénářích zahrnujících přesměrování hovoru, jeho přesměrování nebo připojení k ústředně. Služba je nedílnou součástí signalizace řízení hovoru a primárně využívá protokoly [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) nebo Bearer Independent Call Control (BICC) v jádru sítě.

Z architektonického hlediska je COLI implementována v rámci funkcí řízení hovorové relace sítě, konkrétně v Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) pro CS doménu. Při sestavování hovoru je MSC zapojené do spojení zodpovědné za určení identity konečného spojeného účastníka. Tato informace je následně sdělena zpět signalizační cestou do zdrojového síťového prvku a, pokud je předplatitel přihlášen, volajícímu účastníkovi. Proces zahrnuje analýzu směrování hovoru a všech aktivovaných doplňkových služeb (jako je Call Forwarding Unconditional - [CFU](/mobilnisite/slovnik/cfu/)), aby bylo možné zjistit skutečný koncový bod.

Klíčové komponenty podílející se na poskytování COLI zahrnují MSC, které provádí řízení hovoru a servisní logiku, a Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)), který ukládá profil služeb účastníka a udává, zda je prezentace COLI povolena nebo omezena. Služba interaguje s dalšími doplňkovými službami, jako je Calling Line Identification Presentation ([CLIP](/mobilnisite/slovnik/clip/)) a Connected Line Identification Restriction ([COLR](/mobilnisite/slovnik/colr/)). Samotná data COLI jsou přenášena jako parametr v signalizačních zprávách, jako je Initial Address Message (IAM) a Answer Message (ANM) v ISUP, což zajišťuje jejich dostupnost v okamžiku přijetí hovoru pro síťové zpracování.

Její role v síti přesahuje rámec jednoduché informační služby. COLI je zásadní pro provozní a komerční funkce. Pro síťového operátora umožňuje přesné záznamy o hovorech (CDR) pro účtování, protože poplatky se mohou lišit na základě konečného spojeného čísla, zejména v meziioperátorských scénářích. Také podporuje funkce jako Malicious Call Identification (MCId) a je kritickým vstupem pro systémy zákonného odposlechu (LI), což zajišťuje, že dohled je správně aplikován na skutečně spojeného účastníka. Služba zajišťuje transparentnost a přesnost směrování hovorů, což je nezbytné pro důvěru v telekomunikační služby.

## K čemu slouží

COLI bylo zavedeno, aby vyřešilo zásadní mezeru v telefonních sítích: neschopnost spolehlivě identifikovat, kdo hovor skutečně přijal. V rané telefonii a dokonce i v počátečních digitálních sítích bylo účtování a protokolování hovorů založeno pouze na vytočeném čísle. S příchodem pokročilých funkcí obsluhy hovorů, jako je přesměrování hovoru, přepojení hovoru a přímé vytáčení na linky, však vytočené číslo často neodpovídalo účastníkovi, který hovor přijal. To vytvářelo problémy pro přesnost účtování, detekci podvodů a zákaznický servis.

Historický kontext vzniku COLI spočívá ve vývoji služeb inteligentní sítě a standardizaci služeb ISDN a později okruhově přepínaných služeb 3GPP. Před zavedením COLI čelili operátoři výzvám v oblasti zajištění příjmů, protože hovory přesměrované na čísla s prémiovými sazbami nebo mezinárodní destinace nemohly být správně tarifovány, pokud bylo známo pouze původní vytočené číslo. Dále je pro bezpečnostní a právní účely identifikace skutečně spojené linky zásadní pro sledování zlovolných hovorů nebo přesné provádění příkazů k zákonnému odposlechu.

COLI tyto problémy řeší tím, že poskytuje standardizovaný mechanismus v signalizaci řízení hovoru pro předání ověřené identity spojeného účastníka. Odstraňuje tak omezení předchozích přístupů, které spoléhaly na odvozování nebo analýzu po hovoru, které byly náchylné k chybám a neefektivní. Integrací této identity přímo do signalizační struktury v reálném čase umožňuje COLI přesnou provozní podporu, spravedlivé účtování, vylepšené bezpečnostní funkce a soulad s regulatorními požadavky pro moderní telekomunikační sítě.

## Klíčové vlastnosti

- Poskytuje ověřené telefonní číslo/identitu účastníka, který hovor přijal
- Nezbytná pro přesné generování záznamů o hovorech (CDR) a účtování, zejména pro přesměrované hovory
- Podporuje bezpečnostní funkce jako Malicious Call Identification (MCId)
- Kritický vstup pro systémy zákonného odposlechu (LI) k zaměření na správné spojení
- Funguje prostřednictvím parametrů v signalizačních protokolech řízení hovoru, jako jsou ISUP a BICC
- Spolupracuje s doplňkovými službami CLIP (Calling Line Identification Presentation) a COLR (Connected Line Identification Restriction)

## Související pojmy

- [CLIP – Calling Line Identification Presentation](/mobilnisite/slovnik/clip/)
- [COLR – Connected Line identification Restriction](/mobilnisite/slovnik/colr/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)
- [MCID – Malicious Communication Identity](/mobilnisite/slovnik/mcid/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [COLI na 3GPP Explorer](https://3gpp-explorer.com/glossary/coli/)
