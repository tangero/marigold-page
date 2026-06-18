---
slug: "apri"
url: "/mobilnisite/slovnik/apri/"
type: "slovnik"
title: "APRI – Address Presentation Restriction Indicator"
date: 2025-01-01
abbr: "APRI"
fullName: "Address Presentation Restriction Indicator"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/apri/"
summary: "APRI je signalizační parametr používaný v IP Multimedia Subsystem (IMS) pro řízení viditelnosti informací o adrese volajícího (např. SIP URI, TEL URI) pro volaného účastníka. Umožňuje služby ochrany s"
---

APRI je signalizační parametr IMS, který řídí, zda je volajícího adresa prezentována, zatajena nebo zobrazena pouze s autorizací volanému účastníkovi.

## Popis

Address Presentation Restriction Indicator (APRI) je klíčový parametr v rámci signalizačního rámce Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) v 3GPP IP Multimedia Subsystem (IMS). Funguje jako součást hlavičky P-Asserted-Identity nebo hlavičky From v SIP zprávách, konkrétně v rámci požadavku INVITE, který zahajuje relaci. APRI přenáší preferenci volajícího uživatele týkající se prezentace jeho proklamované identity volanému účastníkovi. Síťové prvky IMS, primárně Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)), tento indikátor interpretují a vynucují na základě uživatelského předplatného, síťové politiky a regulatorních požadavků.

Technicky APRI není samostatná hlavička, ale parametr (často 'privacy') nebo atribut uvnitř identifikačních hlaviček. Jeho hodnoty jsou definovány tak, aby spouštěly konkrétní síťové chování. Pokud je nastaven na 'presentation restricted', síť musí zajistit, že adresa volající strany není volanému uživateli zobrazena. Naopak 'presentation allowed' zobrazení umožňuje. Klíčovou složitost představuje interakce mezi preferencí poskytnutou uživatelem a ověřením a vynucením politiky ze strany sítě. S-CSCF kontroluje proklamovanou identitu vůči profilu uživatele a může přepsat nesprávně uživatelem poskytnutý APRI, aby vyhověl datům předplatného nebo lokální politice, čímž zajišťuje, že ochranu soukromí nelze podvodně vyvolat nebo obejít.

Fungování tohoto mechanismu zahrnuje více uzlů IMS. User Equipment (UE) nebo aplikační server může zahrnout preferenci ochrany soukromí do počátečního SIP požadavku. Jak tento požadavek prochází přes [P-CSCF](/mobilnisite/slovnik/p-cscf/) a S-CSCF vycházející sítě, tyto uzly indikátor zpracovávají. S-CSCF hraje klíčovou roli při aplikaci servisní logiky z uživatelského profilu. Když je požadavek na relaci přeposlán směrem k ukončující síti (potenciálně přes Interrogating-CSCF neboli [I-CSCF](/mobilnisite/slovnik/i-cscf/)), stav APRI je přenášen dál. Ukončující S-CSCF pak podle něj jedná a instruuje ukončující UE, aby buď zobrazilo, nebo skrylo identitu volajícího, často úpravou SIP hlaviček (jako použití hlavičky 'Privacy: id'), které vidí zařízení koncového uživatele.

Role APRI přesahuje základní nastavení hovoru. Integruje se s dalšími mechanismy ochrany soukromí a správy identit v IMS, jako je Asserted Identity a hlavička P-Preferred-Identity. Je nezbytný pro implementaci standardizovaných doplňkových služeb, jako je Calling Line Identification Presentation ([CLIP](/mobilnisite/slovnik/clip/)) a Calling Line Identification Restriction ([CLIR](/mobilnisite/slovnik/clir/)), v prostředí IMS zcela založeném na IP. Jeho správná funkce je povinná pro dodržování regulatorních požadavků v mnoha regionech, kde uživatelé mají zákonné právo zatajit své číslo. APRI je tedy základním, sítí vynucovaným kontrolním bodem pro ochranu soukromí účastníků v moderní telekomunikaci.

## K čemu slouží

APRI byl vytvořen, aby poskytl standardizovaný, na IP založený mechanismus pro ochranu soukromí identity volajícího v rámci architektury 3GPP IMS, a vyřešil tak problém, jak převést tradiční služby ochrany soukromí v telefonii s přepojováním okruhů (jako [CLIR](/mobilnisite/slovnik/clir/)) do světa s přepojováním paketů založeného na [SIP](/mobilnisite/slovnik/sip/). Před IMS byla ochrana soukromí v mobilních sítích řešena specifickou signalizací uvnitř jádra s přepojováním okruhů (např. v MAP nebo ISUP). Migrace na zcela IP jádro (IMS) pro multimediální služby si vyžádala novou metodu fungující s protokoly SIP. APRI to řeší definicí jasného, interoperabilního způsobu signalizace preferencí ochrany soukromí v rámci SIP, což zajišťuje konzistentní chování napříč síťovým vybavením různých dodavatelů a mezi různými operátorskými sítěmi.

Hnací motivací byla potřeba kontinuity služeb a dodržování regulatorních požadavků. Když operátoři nasazovali IMS pro Voice over LTE (VoLTE) a další služby, museli uživatelům nabídnout stejné kontroly ochrany soukromí, jaké měli v legacy sítích. Bez standardu jako APRI by proprietární implementace vedly k problémům s interoperabilitou, nefunkčním funkcím ochrany soukromí při přeshraničních hovorech a neschopnosti splnit legální požadavky na blokování identifikace volajícího. APRI poskytuje potřebnou abstrakci, odděluje záměr uživatele ohledně soukromí od složité síťové logiky potřebné k jeho vynucení, a tím umožňuje spolehlivé a předvídatelné služby ochrany soukromí v ekosystému s více dodavateli a operátory.

APRI navíc řeší omezení jednoduché ochrany soukromí řízené koncovým bodem. V důvěryhodném síťovém modelu, jako je IMS, musí síť identity ověřovat a proklamovat. Povolení koncovému bodu jednostranně skrýt svou identitu by mohlo být zneužito. Návrh APRI zahrnuje vynucení síťové politiky, kde S-CSCF může opravit nebo aplikovat nastavení ochrany soukromí na základě profilu účastníka. To zajišťuje, že ochrana soukromí je službou poskytovanou sítí, nikoli pouze funkcí klienta, což zvyšuje bezpečnost, brání falšování a umožňuje diferenciaci služeb (např. umožňuje, aby prémiová čísla byla vždy prezentována).

## Klíčové vlastnosti

- Signalizuje preferenci ochrany soukromí volajícího v rámci SIP zpráv INVITE
- Vynucuje síťovou politiku prostřednictvím S-CSCF na základě dat uživatelského předplatného
- Umožňuje implementaci doplňkových služeb CLIP/CLIR v IMS
- Podporuje hodnoty pro prezentaci povolenou, omezenou a prezentaci založenou na autorizaci
- Spolupracuje s hlavičkami P-Asserted-Identity a P-Preferred-Identity pro správu identit
- Nezbytný pro dodržování regulatorních požadavků týkajících se ochrany soukromí identifikace volajícího v telefonii založené na IP

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [CLIR – Calling Line Identification Restriction](/mobilnisite/slovnik/clir/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)

## Definující specifikace

- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [APRI na 3GPP Explorer](https://3gpp-explorer.com/glossary/apri/)
