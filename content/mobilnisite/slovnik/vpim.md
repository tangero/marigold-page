---
slug: "vpim"
url: "/mobilnisite/slovnik/vpim/"
type: "slovnik"
title: "VPIM – Voice Profile for Internet Mail"
date: 2005-01-01
abbr: "VPIM"
fullName: "Voice Profile for Internet Mail"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vpim/"
summary: "VPIM je profil 3GPP umožňující přenos hlasových zpráv jako příloh e-mailů přes IP sítě. Standardizuje kódování a zabalení pro interoperabilitu mezi různými systémy hlasové pošty a zasílání zpráv, čímž"
---

VPIM je profil 3GPP, který umožňuje přenos hlasových zpráv jako příloh e-mailů přes IP sítě za účelem zajištění interoperability mezi různými systémy hlasové pošty a zasílání zpráv.

## Popis

Profil hlasové pošty pro internetový e-mail (VPIM) je standardizovaný servisní profil definovaný 3GPP, který specifikuje formátování a přenos hlasových zpráv pomocí internetových poštovních protokolů, především [SMTP](/mobilnisite/slovnik/smtp/) a [MIME](/mobilnisite/slovnik/mime/). Definuje konzistentní metodu pro zapouzdření digitalizovaných hlasových nahrávek spolu s přidruženými metadaty (jako odesílatel, příjemce a časové razítko) do struktury e-mailu. To umožňuje systémům hlasové pošty bezproblémově si vyměňovat zprávy přes různé síťové domény a platformy různých dodavatelů, přičemž je hlasová zpráva chápána jako specializovaná multimediální příloha e-mailu.

Z architektonického hlediska VPIM funguje v rámci servisní vrstvy sítě, často je integrován s centrem služby multimediálních zpráv (MMSC) nebo s vyhrazeným serverem hlasové pošty. Profil vyžaduje použití konkrétních zvukových kodeků, jako je [AMR](/mobilnisite/slovnik/amr/) nebo G.711, pro kódování hlasu, aby byla zajištěna předvídatelná kvalita a schopnost dekódování na přijímací straně. Zapouzdření MIME obsahuje hlavičky typu obsahu identifikující zprávu jako 'audio/vnd.vpim', což směruje přijímací systém k jejímu zpracování jako VPIM-kompatibilní hlasové zprávy namísto generického zvukového souboru.

Během provozu, když uživatel nahraje hlasovou zprávu určenou jinému účastníkovi v jiné síti, zdrojový systém hlasové pošty zakóduje zvuk, zabalí jej podle pravidel VPIM a adresuje jej pomocí adresy ve stylu e-mailu (často odvozené od příjemcova [MSISDN](/mobilnisite/slovnik/msisdn/) nebo vyhrazené VPIM adresy). Zpráva je poté směrována přes standardní internetové poštovní přenosy. Po přijetí VPIM klient cílového systému zprávu dekóduje, extrahuje zvuk a zpřístupní jej v příchozí schránce hlasové pošty příjemce. Tento proces abstrahuje podkladový přenos, což umožňuje hlasovému zasílání zpráv využívat robustní a škálovatelnou e-mailovou infrastrukturu.

Role VPIM je klíčová pro umožnění služeb hlasové pošty napříč sítěmi, zejména v raných scénářích 3G a konvergence pevných a mobilních sítí. Poskytuje most mezi tradiční hlasovou poštou v okruhově spínaných telefonních sítích a IP zasíláním zpráv a podporuje funkce jako indikátor čekající zprávy a oznámení o doručení. Standardizací rozhraní snižuje integrační složitost pro operátory a umožňuje účastníkům přijímat hlasové zprávy i při roamingu mimo přímou servisní oblast domovské sítě.

## K čemu slouží

VPIM byl vytvořen k řešení problému interoperability systémů hlasové pošty. V raných mobilních a pevných telefonních sítích byla hlasová pošta často proprietární, izolovanou službou. Účastník od jednoho operátora nemohl snadno přijmout hlasovou zprávu od účastníka v síti jiného operátora nebo od firemního systému [PBX](/mobilnisite/slovnik/pbx/) bez složitých a nákladných řešení brán. Tato roztříštěnost omezovala užitečnost hlasové pošty jako univerzální služby zasílání zpráv.

Historický kontext představovala konvergence telefonních a internetových technologií na konci 90. let a začátku 21. století. Internet Engineering Task Force ([IETF](/mobilnisite/slovnik/ietf/)) původně vyvinula VPIM jako rozšíření standardního e-mailu ([RFC](/mobilnisite/slovnik/rfc/) 2421, 3801 atd.) pro přenos hlasu. 3GPP tuto práci přijala a profilovala v rámci svých specifikací (počínaje Release 2), aby zajistila, že splňuje specifické požadavky mobilních sítí, jako je adresování založené na [MSISDN](/mobilnisite/slovnik/msisdn/) a integrace s údaji o účastnících z HLR/HSS. To umožnilo mobilním operátorům nabízet 'jednotné zasílání zpráv', kde bylo možné přistupovat k hlasové poště, e-mailům a faxu z jedné příchozí schránky.

Využitím všudypřítomné a spolehlivé přenosové služby e-mailu SMTP poskytl VPIM nákladově efektivní, standardy založenou alternativu k proprietárním protokolům nebo přímým okruhově spínaným spojením pro výměnu hlasové pošty. Vyřešil omezení předchozích přístupů tím, že zajistil, že hlasové zprávy mohou být uloženy, přeposlány a načteny se stejnou spolehlivostí jako e-mail, při zachování přijatelné kvality hlasu a umožnění funkcí jako přeposílání a odpověď na zprávy. Toto byl klíčový krok k plně IP službám zasílání zpráv v sítích 3GPP.

## Klíčové vlastnosti

- Standardizované zapouzdření MIME pro hlasové zprávy jako přílohy e-mailů
- Podpora povinných zvukových kodeků, jako je AMR, pro efektivní využití mobilní šířky pásma
- E-mailové adresování využívající MSISDN nebo VPIM-specifické adresy pro směrování
- Interoperabilita mezi systémy hlasové pošty různých dodavatelů a síťových operátorů
- Podpora oznámení o doručení a synchronizace indikátoru čekající zprávy
- Umožňuje jednotné zasílání zpráv integrací hlasové pošty s e-mailovými infrastrukturami

## Související pojmy

- [MIME – Multi-purpose Internet Mail Extensions](/mobilnisite/slovnik/mime/)

## Definující specifikace

- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition

---

📖 **Anglický originál a plná specifikace:** [VPIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/vpim/)
