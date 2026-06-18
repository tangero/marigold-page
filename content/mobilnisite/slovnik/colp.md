---
slug: "colp"
url: "/mobilnisite/slovnik/colp/"
type: "slovnik"
title: "COLP – Connected Line identification Presentation"
date: 2026-01-01
abbr: "COLP"
fullName: "Connected Line identification Presentation"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/colp/"
summary: "COLP je doplňková služba v sítích 3GPP, která umožňuje volané straně prezentovat své vlastní telefonní číslo volající straně. Je protějškem služby CLIP (prezentace identifikace volající linky) a je kl"
---

COLP je doplňková služba 3GPP, která umožňuje volané straně prezentovat vlastní telefonní číslo volající straně a funguje jako protějšek ke službě CLIP, čímž zajišťuje transparentnost.

## Popis

Connected Line identification Presentation (COLP, prezentace identifikace připojené linky) je standardizovaná doplňková služba definovaná v rámci specifikací 3GPP, která funguje jako součást vrstvy služeb Intelligent Network ([IN](/mobilnisite/slovnik/in/)) a Core Network. Jejím účelem je umožnit síti doručit telefonní číslo (nebo jinou identifikaci) připojené strany – tedy strany, která nakonec hovor přijme – zpět původní volající straně. Tento proces probíhá po dokončení sestavení hovoru a navázání spojení, čímž volajícímu poskytuje ověřovací mechanismus. Služba je typicky vyvolána během sestavování hovoru a spoléhá se na signalizační protokoly jako [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) v okruhově přepínaných doménách nebo Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) v sítích IP Multimedia Subsystem (IMS) pro přenos informací o identifikaci připojené linky.

Z architektonického hlediska COLP interaguje s několika síťovými prvky. V tradičních okruhově přepínaných mobilních sítích zahrnuje Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)). HLR ukládá profil služeb účastníka včetně údajů o předplatném COLP. Když je hovor směrován, obsluhující MSC volané strany načte tento profil a pokud je COLP aktivní, zahrne číslo připojené strany do zpětných zpráv pro sestavení hovoru (např. v ISUP Answer nebo Connect zprávách). V sítích založených na IMS je COLP implementováno pomocí SIP metod a hlaviček, jako je hlavička P-Asserted-Identity, která přenáší ověřenou identitu připojeného uživatele v rámci SIP odpovědí 200 OK na požadavek INVITE.

Provoz služby je úzce spjat s nastavením soukromí a předplatného. Účastník musí mít službu COLP zřízenu a prezentace připojeného čísla může být připojenou stranou omezena pomocí služby Connected Line Identification Restriction ([COLR](/mobilnisite/slovnik/colr/)). Síť provede kontrolu: pokud má připojená strana aktivní COLR, služba COLP číslo volajícímu nezobrazí a místo toho poskytne informaci, že prezentace je omezena. Tato vzájemná součinnost zajišťuje respektování uživatelských nastavení soukromí. Z pohledu volajícího se prezentované číslo připojené linky zobrazí na displeji jeho koncového zařízení, což mu umožní potvrdit, že je spojen s zamýšlenou stranou. To je zásadní pro prevenci podvodů nebo chybného směrování ve scénářích jako je přesměrování hovorů nebo operátorské služby.

Role COLP přesahuje pouhé zobrazení čísla; je základním prvkem pro transparentnost služeb a důvěru. Pokročilé telefonní služby, jako je přesměrování, přepojování hovoru nebo obchodní aplikace, kde hovory přijímá automatický systém nebo operátor, využívají COLP k tomu, aby volajícímu poskytly jistotu o skutečném koncovém bodě, který hovor přijal. Její implementace je pro síťové operátory povinná pro splnění určitých regulatorních požadavků a je klíčovým rozlišovacím znakem prémiových telefonních služeb. Služba funguje v součinnosti s Calling Line Identification Presentation ([CLIP](/mobilnisite/slovnik/clip/)) a vytváří tak obousměrný identifikační rámec, který zlepšuje celkovou uživatelskou zkušenost a bezpečnost telekomunikačních služeb.

## K čemu slouží

COLP bylo vytvořeno, aby vyřešilo asymetrii v službách identifikace volajícího. Zatímco CLIP umožňovalo volané straně vidět, kdo volá, neexistoval standardizovaný mechanismus, který by volající straně umožnil ověřit identitu strany, která hovor skutečně přijala. Tato mezera se stala problematickou s rozšířením přesměrování hovorů, hlasových schránek a operátorských služeb, kde se volající mohl spojit s jiným číslem, než které vytočil. Bez COLP mohli být volající zaváděni, což vedlo k možným podvodům, nejasnostem nebo nedůvěře v telekomunikační služby, zejména v obchodním a nouzovém kontextu.

Služba byla zavedena ve 3GPP Release 99, navazujíc na stávající standardy ISDN, aby poskytla kompletní identifikační rámec. Řeší problém ověření cíle hovoru a zajišťuje uživatelům transparentnost ohledně připojené linky. To je obzvláště důležité pro mobilní sítě, kde jsou funkce jako přesměrování při obsazení nebo nezvednutí běžné. COLP posiluje pozici volajícího tím, že potvrzuje identitu přijímající strany, což zvyšuje bezpečnost proti falšování identity nebo zlovolnému přesměrování a podporuje regulatorní požadavky na trasovatelnost hovorů a ochranu spotřebitele.

Historicky, před zavedením COLP, existovala některá proprietární řešení, ale postrádala interoperabilitu mezi různými síťovými operátory a výrobci zařízení. Standardizace v rámci 3GPP zajistila jednotný přístup, který umožnil bezproblémové poskytování služeb v prostředích s více výrobci a operátory. Integrací COLP do architektury služeb core networku 3GPP odstranila omezení starších systémů, které nedokázaly spolehlivě poskytnout identifikaci připojené strany ve složitých scénářích směrování hovorů, čímž zvýšila spolehlivost a důvěryhodnost telefonních služeb napříč GSM, UMTS a následujícími generacemi.

## Klíčové vlastnosti

- Prezentuje telefonní číslo připojené (odpovídající) strany volající straně
- Funguje jako doplňková služba integrovaná se signalizací pro řízení hovorů
- Spolupracuje se službou Connected Line Identification Restriction (COLR) pro správu soukromí
- Podporována jak v okruhově přepínaných (ISUP), tak v IMS (SIP) síťových doménách
- Vyžaduje zřízení předplatného v HLR nebo uživatelském profilu
- Poskytuje ověření proti scénářům s přesměrováním nebo přepojením hovoru

## Související pojmy

- [CLIP – Calling Line Identification Presentation](/mobilnisite/slovnik/clip/)
- [COLR – Connected Line identification Restriction](/mobilnisite/slovnik/colr/)
- [CLIR – Calling Line Identification Restriction](/mobilnisite/slovnik/clir/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TR 22.976** (Rel-2) — Release 2000 Services Overview
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 29.864** (Rel-8) — Application Server Service Data Definition for IMS Telephony

---

📖 **Anglický originál a plná specifikace:** [COLP na 3GPP Explorer](https://3gpp-explorer.com/glossary/colp/)
