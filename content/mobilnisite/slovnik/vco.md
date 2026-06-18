---
slug: "vco"
url: "/mobilnisite/slovnik/vco/"
type: "slovnik"
title: "VCO – Voice Carry Over"
date: 2025-01-01
abbr: "VCO"
fullName: "Voice Carry Over"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vco/"
summary: "Voice Carry Over je funkce telekomunikační služby pro uživatele se sluchovým nebo řečovým postižením. Umožňuje uživateli mluvit přímo s druhou stranou, zatímco odpověď přijímá jako text, typicky prost"
---

VCO je služba pro uživatele se sluchovým nebo řečovým postižením, která jim umožňuje mluvit přímo s druhou stranou, zatímco odpověď přijímají jako text prostřednictvím přepojovací služby.

## Popis

Voice Carry Over (VCO) je pomocná telekomunikační služba standardizovaná organizací 3GPP pro podporu uživatelů, kteří jsou neslyšící nebo nedoslýchaví, ale mohou mluvit. Při hovoru s VCO uživatel se sluchovým postižením použije svůj hlas, aby mluvil přímo s volanou stranou. Jelikož však nemůže slyšet hlasovou odpověď, je odpověď od volané strany převedena na text a doručena na zařízení uživatele. Tento text se typicky zobrazuje na textovém terminálu, kterým může být specializovaný teletyp ([TTY](/mobilnisite/slovnik/tty/)), smartphone s aplikací pro TTY nebo webové rozhraní přepojovací služby. Převod řeči na text pro uživatele se sluchovým postižením často provádí přepojovací služba obsluhovaná člověkem nebo automatizovaný systém.

Architektura pro VCO zahrnuje několik komponent. Uživatel zahájí hovor, často nejprve vytočením přepojovací služby. Operátor přepojovací služby (nebo automatizovaný systém) poté uskuteční hovor k požadované cílové straně. Jakmile jsou obě spojení navázána, uživatel VCO mluví přímo s cílovou stranou. Řeč cílové strany je směrována do přepojovací služby, kde je přepsána do textu. Tento text je následně odeslán zpět přes síť na textový terminál uživatele VCO. Podpůrná síť musí podporovat simultánní nebo střídavý přenos hlasových a textových datových proudů. To je často umožněno prostřednictvím tónů modemu v pásmu (pro tradiční TTY přes hlasové kanály) nebo modernějšími protokoly pro přenos textu v reálném čase ([RTT](/mobilnisite/slovnik/rtt/)) založenými na IP, které mohou být přenášeny souběžně s hlasem v prostředí IMS/VoLTE.

VCO je klíčovou součástí služeb Total Conversation, jejichž cílem je poskytnout rovnocenný telekomunikační přístup kombinací videa, hlasu a textu v reálném čase. Specifikace 3GPP, jako jsou TS 22.226 a TS 26.226, definují požadavky na službu a kodeky pro VCO a další přepojovací služby. Služba funguje ve spojení s jinými režimy, jako je Hearing Carry Over ([HCO](/mobilnisite/slovnik/hco/)), kde uživatel může slyšet, ale svou odpověď píše. Implementace zajišťuje nízkou latenci při doručování textu, aby byl zachován průběh konverzace, což činí telekomunikace dostupnými a praktickými pro uživatele se specifickým postižením.

## K čemu slouží

Voice Carry Over byl vytvořen, aby řešil významnou mezeru v přístupnosti telekomunikací pro jednotlivce, kteří jsou neslyšící nebo nedoslýchaví, ale zachovali si schopnost mluvit. Tradiční telefonní služby byly zcela založeny na zvuku, což tuto skupinu uživatelů zcela vylučovalo z přímé konverzace. Zatímco textové telefony ([TTY](/mobilnisite/slovnik/tty/)) existovaly, vyžadovaly, aby obě strany měly a používaly TTY, což nebylo praktické pro komunikaci s širokou veřejností. VCO tento problém řeší tím, že umožňuje uživateli se sluchovým postižením využít vlastní hlas, zatímco pro příjem se spoléhá na text, což mu umožňuje komunikovat s kýmkoli prostřednictvím přepojovací služby.

Jeho standardizace v 3GPP, počínaje Release 8, byla motivována právními a regulačními požadavky v mnoha zemích, které vyžadují, aby telekomunikační služby byly přístupné. Řešila omezení předchozích pomocných služeb tím, že poskytovala přirozenější a efektivnější konverzační model ve srovnání s plně textovou přepojovací službou. Integrací VCO do specifikací služeb jádrové sítě zajistilo 3GPP, že mobilní a pevní síťoví operátoři mohou nasadit interoperabilní a spolehlivé funkce přístupnosti, což podporuje sociální začlenění a soulad s legislativou o právech osob se zdravotním postižením.

## Klíčové vlastnosti

- Umožňuje uživatelům se sluchovým postižením mluvit přímo při hovoru.
- Doručuje řeč druhé strany uživateli jako text v reálném čase.
- Typicky funguje s pomocí telekomunikační přepojovací služby.
- Podporuje přenos prostřednictvím tradičních TTY tónů nebo moderního přenosu textu v reálném čase (RTT).
- Může být integrována do sítí IMS/VoLTE pro souběžné hlasové a textové proudy.
- Usnadňuje přirozenější průběh konverzace ve srovnání s čistě textovou přepojovací službou.

## Související pojmy

- [HCO – Hear Carry Over](/mobilnisite/slovnik/hco/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 22.226** (Rel-19) — Global Text Telephony (GTT) Stage 1
- **TS 26.226** (Rel-19) — Cellular Text Telephone Modem (CTM)
- **TS 26.230** (Rel-19) — CTM C Code Implementation for Text Transmission
- **TS 26.231** (Rel-19) — CTM Minimum Performance Requirements Testing

---

📖 **Anglický originál a plná specifikace:** [VCO na 3GPP Explorer](https://3gpp-explorer.com/glossary/vco/)
