<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html>
      <head>
        <link rel="stylesheet" type="text/css" href="style.css"/>
      </head>
      <body>
        <h2>Dades Personals dels Alumnes</h2>
        <table>
          <tr>
            <th>Nom</th>
            <th>Email</th>
            <th>Gènere</th>
          </tr>
          <xsl:apply-templates select="//alumne"/>
        </table>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="alumne">
    <tr>
      <td><xsl:value-of select="nom"/></td>
      <td><xsl:value-of select="email"/></td>
      <td><xsl:value-of select="genere"/></td>
    </tr>
  </xsl:template>

</xsl:stylesheet>
