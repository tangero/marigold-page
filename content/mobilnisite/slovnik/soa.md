---
slug: "soa"
url: "/mobilnisite/slovnik/soa/"
type: "slovnik"
title: "SOA – Suppress Outgoing Access (CUG SS)"
date: 2025-01-01
abbr: "SOA"
fullName: "Suppress Outgoing Access (CUG SS)"
category: "Services"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/soa/"
summary: "Funkce doplňkové služby (SS) Skupiny uzavřených účastníků (CUG), která účastníkovi brání uskutečňovat odchozí hovory na čísla mimo jeho určenou CUG. Vynucuje zákaz uskutečnění hovoru pro odchozí příst"
---

SOA je funkce doplňkové služby Skupiny uzavřených účastníků (CUG SS), která účastníkovi brání uskutečňovat odchozí hovory na čísla mimo jeho určenou skupinu.

## Popis

Suppress Outgoing Access (SOA) je specifická funkce v rámci standardizovaného (3GPP) frameworku doplňkové služby Skupiny uzavřených účastníků ([CUG](/mobilnisite/slovnik/cug/)). CUG je služba, která skupině účastníků poskytuje možnost komunikovat mezi sebou, často s konkrétními výsadami nebo omezeními ve srovnání s veřejnou sítí obecně. SOA je jedno z klíčových omezení, které lze na člena CUG uplatnit. Když je SOA pro účastníka v rámci konkrétní CUG aktivní, je tomuto účastníkovi znemožněno uskutečňovat hovory (nebo někdy i jiné komunikační relace) na destinace, které nejsou součástí této stejné CUG. Vynucení tohoto zákazu provádí páteřní síť, typicky v rámci Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)), v závislosti na generaci sítě (spojově orientovaná nebo založená na IMS).

Fungování SOA je svázáno s profil služeb účastníka, který je uložen v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Když se účastník pokusí zahájit hovor, obslužný síťový uzel jako součást procedury navázání hovoru získá informace o CUG včetně jakýchkoli omezení odchozího přístupu, jako je SOA. Uzel poté analyzuje volané číslo vůči seznamu povolených propojení CUG nebo vůči veřejné síti. Pokud volaná strana není v rámci povolené skupiny a SOA je aktivní, je navázání hovoru zamítnuto. Servisní logika může být složitá, jelikož účastník může být členem více CUG s různým nastavením SOA a precedenční pravidla definovaná ve standardech určují, které omezení se použije.

SOA je základním nástrojem pro vytváření privátních virtuálních sítí v rámci veřejné mobilní infrastruktury. Umožňuje síťovým operátorům a podnikům definovat jasné komunikační hranice. Například společnost může definovat CUG pro své zaměstnance s povolenou funkcí SOA, čímž zajistí, že firemní mobilní telefony nelze použít pro osobní hovory, a tak kontroluje náklady a vynucuje zásady používání. Správa SOA, včetně její aktivace, deaktivace a dotazování, se provádí pomocí standardizovaných řídicích postupů doplňkových služeb, často iniciovaných účastníkem prostřednictvím [USSD](/mobilnisite/slovnik/ussd/) kódů nebo spravovaných síťovým operátorem.

## K čemu slouží

SOA byla vytvořena, aby uspokojila poptávku po řízených komunikačních službách v rámci širší sady funkcí [CUG](/mobilnisite/slovnik/cug/). Podniky a organizace potřebovaly možnost poskytovat mobilní služby zaměstnancům nebo členům s omezeními napodobujícími privátní ústřednu ([PBX](/mobilnisite/slovnik/pbx/)) nebo privátní síť. Primární problém, který SOA řeší, je kontrola nákladů a vynucování zásad tím, že brání neautorizovaným odchozím hovorům na externí, potenciálně drahé destinace, jako jsou mezinárodní čísla nebo služby s prémiovými sazbami.

Historicky, před takovými standardizovanými doplňkovými službami, vyžadovala podobná omezení proprietární řešení nebo fyzické úpravy koncových zařízení, které nebyly škálovatelné. Standardizace CUG a SOA v rámci 3GPP umožnila jednotný, na síť zaměřený přístup k zákazu hovorů, který lze dálkově zřizovat a efektivně spravovat. Odstranila tak omezení základních služeb zákazu hovorů, které byly často vše-nebo-nic, tím, že poskytla podrobnější mechanizmus omezení na bázi skupin. SOA v kombinaci s dalšími funkcemi CUG, jako jsou omezení příchozího přístupu, umožňuje vytvářet sofistikované nabídky virtuálních privátních sítí pro mobilní operátory.

## Klíčové vlastnosti

- Síťově vynucený zákaz odchozích hovorů na destinace mimo Skupinu uzavřených účastníků (CUG) účastníka.
- Integrální součást standardizovaného frameworku doplňkové služby (SS) CUG.
- Specifické pro účastníka zřizované a uložené v HLR/HSS.
- Vynucení řízení hovoru na MSC nebo CSCF během zahájení hovoru.
- Podpora složitých scénářů s členstvím ve více CUG a precedenčními pravidly.
- Dálková správa prostřednictvím standardizovaných řídicích postupů doplňkových služeb.

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [USSD – Unstructured Supplementary Services Data](/mobilnisite/slovnik/ussd/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.085** (Rel-19) — Closed User Group (CUG) Supplementary Service Stage 2
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.824** (Rel-9) — SOA and IRP Gap Analysis
- **TS 32.832** (Rel-10) — Alarm Correlation and Root Cause Analysis Study

---

📖 **Anglický originál a plná specifikace:** [SOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/soa/)
