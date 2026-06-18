---
slug: "d-csi"
url: "/mobilnisite/slovnik/d-csi/"
type: "slovnik"
title: "D-CSI – Dialled Services CAMEL Subscription Information"
date: 2025-01-01
abbr: "D-CSI"
fullName: "Dialled Services CAMEL Subscription Information"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/d-csi/"
summary: "D-CSI je parametr předplatného CAMEL, který umožňuje registru domovské polohy (HLR) informovat navštívené mobilní ústředí (VMSC) o potřebě vyvolat služby CAMEL pro konkrétní volaná čísla. Je klíčový p"
---

D-CSI je parametr předplatného CAMEL, který umožňuje HLR informovat VMSC o nutnosti vyvolání služeb CAMEL pro volání iniciovaná mobilním účastníkem na základě konkrétního volaného čísla.

## Popis

Dialled Services [CAMEL](/mobilnisite/slovnik/camel/) Subscription Information (D-CSI, informace o předplatném služeb CAMEL pro volaná čísla) je specifický typ dat předplatného CAMEL uložený v registru domovské polohy ([HLR](/mobilnisite/slovnik/hlr/)) pro mobilního účastníka. Je součástí širšího rámce CAMEL (Customised Applications for Mobile networks Enhanced Logic), který umožňuje operátorům sítí nasazovat služby inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) v prostředí mobilních sítí GSM/UMTS. Hlavní funkcí D-CSI je spouštět servisní logiku CAMEL pro volání iniciovaná mobilním účastníkem na základě vytočeného cílového čísla. Když účastník zahájí hovor, navštívené mobilní ústředí ([VMSC](/mobilnisite/slovnik/vmsc/)) obsluhující tohoto účastníka dotazuje HLR na data účastníka. Pokud je v profilu účastníka přítomno D-CSI, HLR jej zahrne do odpovědi odeslané VMSC.

Z architektonického hlediska D-CSI funguje v rámci protokolového rámce CAMEL Application Part ([CAP](/mobilnisite/slovnik/cap/)) mezi VMSC (které vystupuje jako gsmSSF - GSM Service Switching Function) a vyhrazeným externím uzlem zvaným gsmSCF (GSM Service Control Function). Samotná data D-CSI obsahují klíčové parametry, jako je adresa gsmSCF (číslo E.164 nebo IP adresa uzlu řízení služeb), servisní klíč (identifikující konkrétní službu CAMEL k vyvolání) a především sada spouštěčů volaných čísel. Tyto spouštěče jsou typicky definovány jako seznamy cílových čísel nebo číselných rozsahů (např. prémiová čísla, mezinárodní předvolby, čísla specifických služeb). D-CSI může také zahrnovat další parametry specifické pro CAP, jako jsou výchozí instrukce pro zpracování hovoru a indikátor zpracování schopností CAMEL.

Když VMSC obdrží od účastníka požadavek na sestavení hovoru, porovná volané číslo se spouštěči uvedenými v D-CSI. Pokud je nalezena shoda, VMSC pozastaví běžné zpracování hovoru a zahájí dialog CAMEL s určeným gsmSCF. VMSC odešle gsmSCF operaci CAP InitialDP (Initial Detection Point) obsahující volané číslo, volající číslo a další relevantní podrobnosti o hovoru. gsmSCF, který hostuje vlastní servisní logiku (např. pro řízení předplaceného kreditu, zákaz hovorů nebo překlad čísel), poté převezme kontrolu nad hovorem. Může instruovat VMSC, aby pokračovalo, uvolnilo nebo upravilo hovor (např. připojilo se k jinému cíli, přehrálo oznámení) prostřednictvím následných operací CAP, jako jsou RequestReportBCSMEvent, ApplyCharging a Connect.

Role D-CSI se liší od jiných spouštěčů CAMEL, jako je [O-CSI](/mobilnisite/slovnik/o-csi/) (pro volání iniciovaná účastníkem) nebo [T-CSI](/mobilnisite/slovnik/t-csi/) (pro volání přijímaná účastníkem). Poskytuje detailní, číslo-specifickou kontrolu pro odchozí hovory. To operátorům umožňuje aplikovat různé tarify, zásady zákazů nebo způsoby zpracování služeb v závislosti na tom, zda uživatel volá na místní číslo, mezinárodní číslo nebo specifickou službu, jako je hlasová schránka nebo zákaznická podpora. Jeho implementace je základním kamenem pro umožnění pokročilých, v reálném čase probíhajících, na účastníka specifických služeb, které nejsou nativně podporovány základními protokoly pro řízení hovorů GSM/UMTS, a tím efektivně rozšiřuje servisní schopnosti sítě bez nutnosti aktualizace každé ústředny.

## K čemu slouží

D-CSI bylo vytvořeno, aby řešilo potřebu inteligentního, na cíl zaměřeného řízení hovorů a účtování v sítích GSM a raného UMTS. Před [CAMEL](/mobilnisite/slovnik/camel/) a spouštěči jako je D-CSI byly služby mobilních sítí z velké části statické a založené na profilech předplatného v HLR/VMSC. Implementace dynamických služeb, jako je účtování předplacených služeb v reálném čase, filtrování hovorů na základě volaných čísel nebo vlastní směrování hovorů, vyžadovala proprietární, na dodavatele specifická řešení, která bylo obtížné standardizovat a zajistit jejich interoperabilitu mezi různým síťovým vybavením od více výrobců.

Zavedení D-CSI jako součásti CAMEL fáze 2 a 3 (specifikované ve 3GPP Release 4 a 5) poskytlo standardizovaný mechanismus pro přesunutí komplexní servisní logiky z jádrových ústředen (MSC) na vyhrazené, centralizované servisní platformy (gsmSCF). Tím se vyřešil problém pomalého nasazování služeb a závislosti na jednom dodavateli. Konkrétně D-CSI vyřešilo problém aplikace různých politik na různé typy volaných čísel. Například operátor mohl použít D-CSI k zajištění, že hovory na prémiová čísla jsou povoleny pouze v případě, že předplacený účastník má dostatečný kredit, zatímco hovory na tísňová čísla jsou vždy povoleny bez jakékoli kontroly kreditu. Umožnilo to vytváření sofistikovaných tarifních plánů, kde cena za minutu závisí na vytočeném cílovém čísle.

Historicky bylo vytvoření D-CSI motivováno komerčním úspěchem předplacených mobilních služeb a potřebou flexibilnějšího prostředí pro tvorbu služeb. Umožnilo operátorům rychle nasazovat a zpeněžovat nové přidané služby, jako jsou slevy věrnostní zákazníků založené na volaném čísle, rodičovské kontroly (zákaz volání na určitá čísla) a inteligentní přesměrování hovorů na základě volaného cíle. Standardizací tohoto spouštěcího mechanismu zajistilo 3GPP, že servisní logika vyvinutá pro jednu síť může v principu fungovat s ústřednami od jiného dodavatele, což podpořilo konkurenci a inovace na trhu služeb inteligentní sítě.

## Klíčové vlastnosti

- Spouští vyvolání služby CAMEL na základě konkrétních volaných cílových čísel nebo číselných rozsahů
- Obsahuje adresu (adresu gsmSCF) externího uzlu řízení služeb hostujícího inteligentní logiku
- Zahrnuje parametr servisního klíče pro identifikaci konkrétní CAMEL aplikace k provedení
- Umožňuje řízení hovorů, účtování a interakci v reálném čase pod kontrolou gsmSCF pro volání iniciovaná mobilním účastníkem
- Umožňuje cílově specifické fakturační politiky, jako jsou různé sazby pro místní, tuzemské a mezinárodní hovory
- Podporuje pokročilé služby, jako je předplacené účtování, filtrování/zákaz hovorů a překlad volaných čísel

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [O-CSI – Originating CAMEL Subscription Information](/mobilnisite/slovnik/o-csi/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [D-CSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/d-csi/)
